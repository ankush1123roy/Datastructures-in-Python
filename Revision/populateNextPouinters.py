
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

	def BFS(self, node):
		if node:
			Q = node
			NODES = []
			NODES.append([Q])
			temp = [Q]
			while 1:
				import pdb;pdb.set_trace()
				BUFF = []
				while len(temp) > 0:
					NODE = temp.pop(0)
					if NODE.left:BUFF.append(NODE.left)
					if NODE.right:BUFF.append(NODE.right)
				NODES.append(BUFF)
				if len(BUFF) > 0:
					temp = BUFF
				else:
					break
			return NODES

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
	
	







			

