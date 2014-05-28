'''This is a library for Binary Search Trees
	Each Node has three fields

	Node
	----

	1. Data
	2. Left Pointer (Pointer to left Child)
	3. Right Pointer (Pointer to right Child)
	4. Level (Denotes the level of the tree)


	Class BST has the following methods
	-----------------------------------

	1. Insert a new node in a BST		(DONE)
	2. Delete a node from a BST	
	3. Inorder Traversal of a BST 		(DONE)
	4. Preorder Traversal of a BST		(DONE)
	5. Postorder traversal of a BST		(DONE)
	6. Leveloredr traversal of a BST	(DONE)
	7. Mirror of a BST					(DONE)
	8. Search for an Element in a BST	(DONE)
	9. Lowest Common Ancestor of a BST	(DONE)
	10. Height of a BST					(DONE)
	11. Circumference of a BST 			(DONE)
	12. Diameter of a BST				(DONE)

'''


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
	
	







			

