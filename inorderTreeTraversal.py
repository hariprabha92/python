# inorder traversal

class Node:

	def _init_(self,data):
		self.left = None
		self.right = None
		self.data =data
	def insert(data,self):
		if self.data:
			if data < self.data:
				if self.data is None:
					self.left = Node(data)
				else:
					self.insert(data)
			else if data > self.data:
				if self.data is None:
					self.right	= Node(data)
				else:
					self.insert(data)

		else:
			self.data = data

	def printTree(self):
		if self.left :
			print self.left.printTree
		print(self.data)
		if self.right:
			print self.right.printTree
	def inorderTraversal:
		res = []
		if root:
			res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
