'''
Implementation of a stack and queue.
'''

class Node(object):
	def __init__(self, val=None, next=None):
		self.val = val
		self.next = next


class Stack(object):
	def __init__(self, top=None):
		self.top = top

	def push(self, new_val):
		new_node = Node(new_val, self.top)
		self_top = new_node

	def pop(self):
		if self.top:
			removed = self.top.val
			self.top = self.top.next
		else:
			raise Exception("Empty stack!")

	def length(self):
		count = 0
		curr = self.top
		while curr:
			count += 1
			curr = curr.next
		return count


class Queue(object):
	def __init__(self, first=None):
		self.first = first
		self.last = None

	def add(self, new_val):
		new_node = Node(new_val)
		if self.last:
			self.last.next = new_node
			self.last = new_node
		else:
			self.first.next = new_node

	def remove(self):
		if self.first:
			removed = self.first.val
			self.first = self.first.next
		else:
			raise Exception("Empty queue!")

	def length(self):
		count = 0
		curr = self.first
		while curr:
			count += 1
			curr = curr.next
		return count




