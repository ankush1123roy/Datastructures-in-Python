


class Node():
	def __init__(self,data):
		self.data = data
		self.right  = None
		self.left = None
		self.level = None

	def __str__(self):
		return str(self.data)

class BST():

	def __init__(self):
		self.root = None

	def Insert(self,val):

		'''
		Insert an element in a BST in O(log n)
		No Duplicates are allowed in this case
		'''
		
		if self.root == None:
			self.root = Node(val)
		else:
			present = self.root
			while 1:
				if val < present.data:
					if present.left:
						present = present.left
					else:
						present.left = Node(val)
						break

				elif val > present.data:
					if present.right:
						present = present.right
					else:
						present.right = Node(val)
						break
				else:
					break
		return self.root

	
	def postOrder(self, node, sol):
		if node != None:
			self.postOrder(node.left, sol)
			self.postOrder(node.right, sol)
			sol.append(node.val)
		return sol
	
	def inOrder(self, node, sol):
		if node != None:
			self.inOrder(node.left, sol)
			sol.append(node.val)
			self.inOrder(node.right, sol)
		return sol
	
	def preOrder(self, node, sol):
		if node != None:
			sol.append(node.val)
			self.preOrder(self, node.left, sol)
			self.preOrder(self, node.rigth, sol)
		return sol

if __name__ == '__main__':
	A = [4,2,3,1,9]
	B = BST()
	for i in A:
		T = B.Insert(i)
	print B.postOrder(T, sol = [])
	
	







			

