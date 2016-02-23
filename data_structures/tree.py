'''
Implementation of a binary tree.
'''

class Node(object):
	def __init__(self, val=None):
		self.left = None
		self.right = None
		self.val = val


class Tree(object):
	def __init__(self, root=None):
		self.root = root

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

	def dfs_preorder(self):
		pass

	def dfs_inorder(self):
		pass

	def dfs_postorder(self):
		pass	

	def bfs(self):
		pass

	def delete_tree(self):
		self.root = None
