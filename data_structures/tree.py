'''
Implementation of a binary tree.
'''

class Node(object):
	def __init__(self, val=None):
		self.left = None
		self.right = None
		self.val = val


class Tree(object):
	def __init__(self):
		self.root = None

	def get_root(self):
		return self.root

	def add(self, new_val):
		if not self.root:
			self.root = Node(new_val)
		else:
			self._add(new_val, self.root)

	def _add(self, new_val, curr_node):
		if new_val < curr_node.val:
			if curr_node.left:
				self._add(new_val, curr_node.left)
			else:
				curr_node.left = Node(new_val)
		else:
			if curr_node.right:
				self._add(new_val, curr_node.right)
			else:
				curr_node.right = Node(new_val)

	def find(self, val):
		if not self.root:
			raise Exception("Empty tree!")
		else:
			node = None
			if val == self.root.val:
				return self.root
			elif val < self.root.val:
				node = self._find(val, self.root.left)
			else:
				node = self._find(val, self.root.right)

			if node:
				return node
			else:
				raise Exception("Tree does not contain value.")

	def _find(self, val, curr_node):
		if curr_node:
			if val == curr_node.val:
				return curr_node
			elif val < curr_node.val:
				self._find(val, curr_node.left)
			else:
				self._find(val, curr_node.right)
		else:
			return None


	'''
		Preorder traversal:
		1) Display data of root/current node
		2) Traverse left sub-tree with recursive preorder
		3) Traverse right sub-tree with recursive preorder
	'''
	def dfs_preorder(self):
		order = []
		curr_node = self.root
		self._preorder(curr_node, order)
		return order

	def _preorder(self, curr_node, order):
		if curr_node:
			order.append(curr_node.val)
		if curr_node.left:
			self._preorder(curr_node.left, order)
		if curr_node.right:
			self._preorder(curr_node.right, order)

	def dfs_preorder_iterative(self):
		order = []
		node_stack = [self.root]
		while node_stack:
			curr_node = node_stack.pop()
			if curr_node.right:
				node_stack.append(curr_node.right)
			if curr_node.left:
				node_stack.append(curr_node.left)
			if curr_node:
				order.append(curr_node.val)
		return order

	'''
		Inorder traversal:
		1) Traverse left sub-tree with recursive inorder
		2) Display data of root/current node
		3) Traverse right sub-tree with recursive inorder
	'''
	def dfs_inorder(self):
		order = []
		curr_node = self.root
		self._inorder(curr_node, order)
		return order

	def _inorder(self, curr_node, order):
		if curr_node.left:
			self._inorder(curr_node.left, order)
		if curr_node:
			order.append(curr_node.val)
		if curr_node.right:
			self._inorder(curr_node.right, order)

	def dfs_inorder_iterative(self):
		order = []
		node_stack = []

		curr_node = self.root

		while node_stack or curr_node:
			if curr_node:
				node_stack.append(curr_node)
				curr_node = curr_node.left
			else:
				curr_node = node_stack.pop()
				order.append(curr_node.val)
				curr_node = curr_node.right

		return order

	'''
		Postorder traversal:
		1) Traverse left sub-tree with recursive postorder
		2) Traverse right sub-tree with recursive postorder
		3) Display data of root/current node
	'''
	def dfs_postorder(self):
		order = []
		curr_node = self.root
		self._postorder(curr_node, order)
		return order	

	def _postorder(self, curr_node, order):
		if curr_node.left:
			self._postorder(curr_node.left, order)
		if curr_node.right:
			self._postorder(curr_node.right, order)
		if curr_node:
			order.append(curr_node.val)

	def dfs_postorder_iterative(self):
		order = []
		visited = []
		node_stack = [self.root]
		while node_stack:
			curr_node = node_stack.pop()
			if curr_node.left and curr_node.right:
				visited.append(curr_node.val)
				node_stack.append(curr_node.right)
				node_stack.append(curr_node.left)
			elif curr_node.right:
				order.append(visited.pop())
				visited.append(curr_node.val)
				node_stack.append(curr_node.right)
			elif curr_node.left:
				visited.append(curr_node.val)
				node_stack.append(curr_node.left)
			else:
				order.append(curr_node.val)

		while visited:
			order.append(visited.pop())

		return order

	'''
		BFS traversal:
		Use queue to traverse nodes in level order
	'''	
	def bfs(self):
		order = []
		node_queue = [self.root]
		while node_queue:
			curr_node = node_queue[0]
			node_queue = node_queue[1:]
			order.append(curr_node.val)
			if curr_node.left:
				node_queue.append(curr_node.left)
			if curr_node.right:
				node_queue.append(curr_node.right)
		return order

	def delete_tree(self):
		self.root = None


tr = Tree()
tr.add(4)
tr.add(2)
tr.add(1)
tr.add(3)
tr.add(6)
tr.add(8)
tr.add(7)

'''
Visual of tree
	  4
   2     6
 1	 3	    8
		  7
'''

print "Preorder: {}".format(tr.dfs_preorder())
print "Preorder Iterative: {}".format(tr.dfs_preorder_iterative())
print "Inorder: {}".format(tr.dfs_inorder())
print "Inorder Iterative: {}".format(tr.dfs_inorder_iterative())
print "Postorder: {}".format(tr.dfs_postorder())
print "Postorder Iterative: {}".format(tr.dfs_postorder_iterative())
print "BFS (level order): {}".format(tr.bfs())


