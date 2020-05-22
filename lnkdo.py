import time

class Node(object):
	''' Defines a task object for the ToDoList class '''

	def __init__(self, data=None, complete=False): 
		''' Constructor: input data (holds the task), complete (checks if taks is completed),
		    next (points to the following node) '''
		self.index = 0
		self.data = data
		self.complete = complete
		self.time = time.strftime('%b %d, %Y %I:%M%p')
		self.next = None

	def __repr__(self):
		''' Returns an object representation of the class. '''
		return '{self.__class__.__name__}({self.data}, {self.complete})'.format(self=self)


class ToDoList(object):
	''' Defines a ToDoList object. '''

	def __init__(self):
		''' Constructor: By default, a new list starts with an empty initial node (head). '''
		self.head = Node()
	

	def __repr__(self):
		''' Returns an object representation of the class. '''
		
		return '{self.__class__.__name__}({self.head})'.format(self=self)


	def __str__(self):
		''' Returns a string representation of the ToDoList. '''
		todo = ''
		separator = '-'*80
		#Pointer 'current_node' points to the beginning of the list
		current_node = self.head
	
		if current_node.next == None:
			return '{self.__class__.__name__} is empty.'.format(self=self)
		else:
			self.indexNodes()			
			while current_node.next != None:
				current_node = current_node.next
				todo += '\n   %-4d | %-30s | %-11s | %-30s' % (current_node.index, current_node.data, current_node.complete, current_node.time)
		
		return('  \n   %-4s | %-30s | %-10s | %-30s \n' % ('#', '-Task-', '-Completed-', '-Added Date-') + separator + todo)


	def addTask(self, newtask):
		''' Adds a new task to the end of to-do list. '''

		#Pointer 'current_node' points to the beginning of the list
		current_node = self.head
		#Creates new node hoding the new task
		new_task = Node(data=newtask)
	
		#Travels to the end of the list
		while current_node.next != None:
			current_node = current_node.next

		#Add the new task to the end of the list
		current_node.next = new_task


	def findTaskByDescription(self, task):
		''' Find a task in the list by description. '''

		self.indexNodes()
		current_node = self.head

		while current_node.next != None:
			current_node = current_node.next
			if current_node.data == task:
				return current_node.index

		if current_node.data != task and current_node.next == None:
			return f'***"{task}" is not in the list.***'


	def findTaskByIndex(self, indx):
		''' Find a task in the list by position (index). '''
		idx = int(indx)
		self.indexNodes()
		current_node = self.head

		while current_node.next != None:
			current_node = current_node.next
			if current_node.index == idx:
				return current_node.data

		if current_node.index != idx and current_node.next == None:
			return f'***"{idx}" is not a position the list.***'


	def checkTask(self, task):
		''' Allows a given task to be checked as completed. '''
		found_task = findTaskByDescription(task)
		found_task.complete = True

		print(f'***"{task}" has been marked as completed.***')


	def unCheckTask(self, task):
		''' Allows a given task to be unchecked as incompleted. '''
		found_task = findTaskByDescription(task)
		found_task.complete = False

		print(f'***"{task}" has been marked as incompleted.***')

	def indexNodes(self):
		''' Provides a secuential index to ToDoList nodes. '''
		idx = 0
		current_node = self.head 

		while current_node.next != None:
				idx += 1
				current_node = current_node.next
				current_node.index = idx






td = ToDoList()
td.addTask("comprar")
td.addTask("correr")
td.addTask("hacer cena")
print("\n Index of 'correr' is: ", td.findTaskByDescription("correr"))
print("\n Task of index 2 is: ", td.findTaskByIndex(2))

print(td)

