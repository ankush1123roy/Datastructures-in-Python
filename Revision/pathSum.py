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
		if node.left == None and node.right == None and target - node.val == 0:
				return True
		else:
			return self.pathSum(node.left, target - node.val) or self.pathSum(node.right, target - node.val)
		
			

if __name__ == '__main__':
	A = [4,2,3,1,9]
	B = BST()
	for i in A:
		T = B.Insert(i)
	bftTree = B.BFS(T)
	for i in BFT:
		ROW = i
		for i in range(len(ROW) - 1):
			ROW[i].next = ROW[i+1]
	
	







			

