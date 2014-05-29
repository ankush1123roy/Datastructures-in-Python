'''
This works for both 
Populate Next Pointers and 
Populate Next Pointers II
'''
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

	def pathSum(self, node, target):
		if node == None:
			return False
		else:
			if node.left == None and node.right == None and target - node.data == 0:
					return True
			else:
				return self.pathSum(node.left, target - node.data) or self.pathSum(node.right, target - node.data)
	
	def pathSum2(self, node, target, sol, temp):
		if node == None:
			return 
		else:
			if node.left == None and node.right == None and target - node.data == 0:
				temp.append(node.data)
				sol.append(temp)
			else:
				self.pathSum2(node.left, target - node.data, sol, temp + [node.data])
				self.pathSum2(node.right, target - node.data, sol, temp + [node.data]) 
		return sol

if __name__ == '__main__':
	A = [8, 4, 7, 11]
	B = BST()
	for i in A:
		T = B.Insert(i)
	print B.pathSum(T, 19)
	print B.pathSum2(T, 19, sol = [], temp = [])
	
	







			

