'''
Implementation of Doubly Linked List.
'''

class Node(object):
	
	def __init__(self, data=None):
		self.data = data
		self.prev = None
		self.next = None

	def get_data(self):
		return self.data

	def get_prev(self):
		return self.prev

	def get_next(self):
		return self.next

	def set_data(self, new_data):
		self.data = new_data

	def set_prev(self, new_node):
		self.prev = new_node

	def set_next(self, new_node):
		self.next = new_node


class LinkedList(object):
	
	def __init__(self, head=None):
		self.head = head


	# Return the size of the linked list
	def size(self):
		curr_node = self.head
		count = 0
		while curr_node:
			count += 1
			curr_node = curr_node.get_next()
		return count


	# Insert new Node at specified index, otherwise raise error if index out of bounds
	def insert(self, index, new_data):
		if index < 0 or index > self.size():
			raise Exception("Index out of bounds.")

		new_node = Node(new_data)
		if index == 0:
			new_node.set_next(self.head)
			new_node.get_next().set_prev(new_node)
			self.head = new_node
		else:
			prev_node = self.search(index-1, True)
			new_node.set_next(prev_node.get_next())
			new_node.set_prev(prev_node)
			prev_node.set_next(new_node)


	# Return data from Node specified at index, otherwise raise error if index out of bounds
	def search(self, index, return_node=False):
		if index < 0 or index > self.size():
			raise Exception("Index out of bounds.")

		curr_node = self.head
		curr_index = 0
		while curr_index != index:
			curr_node = curr_node.get_next()
			curr_index += 1

		return curr_node if return_node else curr_node.get_data()
			


	# Delete Node containing data, otherwise raise error if not found
	def delete(self, data):
		curr_node = self.head
		prev = None
		found = False
		while curr_node and not found:
			if curr_node.get_data() == data:
				found = True
			else:
				prev = curr_node
				curr_node = curr_node.get_next()

		if curr_node == None:
			raise Exception("No such data in list.")
		elif prev == None:
			self.head = curr_node
			self.head.set_prev(None)
		else:
			prev.set_next(curr_node.get_next())
			prev.get_next().set_prev(prev) 
	
	# Custom string method to print out data in list
	def __str__(self):
		l = []
		curr_node = self.head
		while curr_node:
			l.append(str(curr_node.get_data()))
			curr_node = curr_node.get_next()
		return "(" + ",".join(l) + ")"



ll = LinkedList()
ll.insert(0,0)
ll.insert(1,1)
ll.insert(2,2)
print ll
ll.insert(1,0.5)
print ll.search(1)

