#Pre order ttraversal
#the root node is visited first, then the left subtree and finally the right subtree.


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
					self.left.insert(data)

			elif data > self.data :
				if self.data is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
			else:
				self.data=data
	def printTree(self):
		if self.left:
			self.left.printTree()
		print(self.data),
		if self.right:
			self.right.printTree()
	def preorderTraversal(self,data):
		res = []
		if root:
			res.append(root,data)
			res = res + self.preorderTraversal(root.left)
			res =res + self.preorderTraversal(root.right)
		return res
		





