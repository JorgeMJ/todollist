import time

class Node(object):
	''' Defines a task object for the ToDoList class '''

	def __init__(self, data=None, complete=False): 
		''' Constructor: input data (holds the task), complete (checks if taks is completed),
		    next (points to the following node) '''
		self.data = data
		self.complete = complete
		self.time = time.strftime('%b %d, %Y %I:%M%p %z')
		self.next = None

	def __repr__(self):
		''' Returns an object representation of the class. '''
		return '{self.__class__.__name__}({self.data}, {self.complete})'.format(self=self)


class ToDoList(object):
	''' Defines a ToDoList object. '''

	def __init__(self):
		''' Constructor: By default, a new list starts with an empty initial node (head). '''
		self.head = Node()

	def newTask(self, newtask):
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
	
	def __repr__(self):
		''' Returns an object representation of the class. '''
		return '{self.__class__.__name__}({self.head})'.format(self=self)

	def __str__(self):
		
		todo = ''
		#Pointer 'current_node' points to the beginning of the list
		current_node = self.head

		if current_node.next == None:
			return '{self.__class__.__name__} is empty.'.format(self=self)
		else:			
			while current_node.next != None:
				current_node = current_node.next
				todo += f'\n{current_node.data}, {current_node.complete}, {current_node.time}'
		
		return todo

td = ToDoList()
td.newTask("comprar")
td.newTask("correr")
td.newTask("hacer cena")

print(td)
do