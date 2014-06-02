
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

	def allPaths(self, node, temp, sol):
		if node != None:
			self.allPaths(node.left, temp + [node.data], sol)
			self.allPaths(node.right, temp + [node.data], sol)
			if node.left == None and node.right == None:
				temp.append(node.data)
				sol.append(sum(temp))
		return sum(sol)

		
			

if __name__ == '__main__':
	A = [4,2,3,1,9]
	B = BST()
	for i in A:
		T = B.Insert(i)
	print B.allPaths(T, temp = [], sol = [])
	
	







			

