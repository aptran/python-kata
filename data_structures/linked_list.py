'''
Implementation of Singly Linked List.
'''

class Node(object):
	
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_data(self, new_data):
		self.data = new_data

	def set_next(self, new_node):
		self.next_node = new_node


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
			self.head = new_node
		else:
			prev_node = self.search(index-1, True)
			new_node.set_next(prev_node.get_next())
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
		else:
			prev.set_next(curr_node.get_next()) 
			




