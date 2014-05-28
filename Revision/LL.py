class Node():
	
	def __init__(self, val):
		self.val = val
		self.next = None
	
class LL():
	
	def __init__(self):
		self.root = None
	
	def Insert(self, val):
		NEW = Node(val)
		if self.root == None:
			self.root = NEW
		else:
			NEW.next = self.root
			self.root = NEW
		return self.root
	
	def Print(self, node):
		if node != None:
			print node.val
			self.Print(node.next)
