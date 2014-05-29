
class Node():
	def __init__(self,data):
		self.data = data
		self.right  = None
		self.left = None
		self.next = None
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

	def validateBST(self, node):
		ARRAY = self.inOrder(node, temp = [])
		for i in range(len(ARRAY) - 1):
			if ARRAY[i+1] < ARRAY[i]:
				return False
		return True
		
	def inOrder(self, node, temp):
		if node != None:
			self.inOrder(node.left, temp)
			temp.append(node.data)
			self.inOrder(node.right, temp)
		return temp

if __name__ == '__main__':
	A = [4,2,3,1,9]
	B = BST()
	for i in A:
		T = B.Insert(i)
	print B.validateBST(T)

	
	







			

