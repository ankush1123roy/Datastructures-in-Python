'''
   Binary Search Tree
   No Duplicate Values are allowed in BST. So its an ordered BST
   ------------------
Author: ankush2@ualberta.ca  
'''
import sys
class Node:

		def __init__(self,info): 

			self.info = info  
			self.left = None  
			self.right = None 
			self.level = None 

		def __str__(self):
			return str(self.info)

class BinarySearchTree:

		def __init__(self): 
			self.root = None

		def create(self,val):
			if self.root == None:
				self.root = Node(val)
			else:
				current = self.root
				while 1:
					if val < current.info:
						if current.left:
							current = current.left
						else:
							current.left = Node(val)
							break;      
					elif val > current.info:
						if current.right:
							current = current.right
						else:
							current.right = Node(val)
						break;      
					else:
						break 
			return self.root

		def bft(self): 
			self.root.level = 0 
			queue = [self.root]
			out = []
			current_level = self.root.level
			while len(queue) > 0:
				current_node = queue.pop(0)
				if current_node.level > current_level:
					current_level += 1
					out.append("\n")
				out.append(str(current_node.info) + " ")
				if current_node.left:
					current_node.left.level = current_level + 1
					queue.append(current_node.left)

				if current_node.right:
					current_node.right.level = current_level + 1
					queue.append(current_node.right)
					
			print "".join(out)





		def lca(self,node, n1, n2):
			if self.match(node.left, n1) and self.match(node.left, n2):
					return self.lca(node.left, n1, n2) # until we find the least common ancestor by node.left
			if self.match(node.right, n1) and self.match(node.right, n2):
					return self.lca(node.right, n1, n2) # until we find the least common ancestor by node.right
			return node
                        
		def match(self,node, n):
			if node is None: return False
			if node == n: return True
			return match(node.left) or match(node.rigth)

		def newOrdering(self):
			self.root.level = 0
			queue = [self.root]
			out = []
			current_level = self.root.level
			while len(queue) > 0:
					current_node = queue.pop(0)
					if current_node.level > current_level:
						current_level += 1
						out.append("\n")
					out.append(str(current_node.info) + " ")

					if current_node.right:
						current_node.right.level = current_level + 1
						queue.append(current_node.right)

					if current_node.left:
						current_node.left.level = current_level + 1
						queue.append(current_node.left)
#                  import pdb;pdb.set_trace()
#                  if current_level %2 == 1:
#                        if current_node.left:
#                              current_node.left.level = current_level + 1
#                              queue.append(current_node.left)
#
#                        if current_node.right:
#                              current_node.right.level = current_level + 1
#                              queue.append(current_node.right)
#                  else:
#                        if current_node.right:
#                              current_node.right.level = current_level + 1
#                              queue.append(current_node.right)
#
#                        if current_node.left:
#                              current_node.left.level = current_level + 1
#                              queue.append(current_node.left)
			print "".join(out)

		def inorder(self,node):
			if node is not None:
				self.inorder(node.left)
				print node.info
				self.inorder(node.right)

		def preorder(self,node):
			if node is not None: 
				print node.info
				self.preorder(node.left)
				self.preorder(node.right)
              
		def postorder(self,node):
			if node is not None:
				self.postorder(node.left)
				self.postorder(node.right)
				print node.info

		def query(self,node,val):
			ROOT = node
			if ROOT == None:
					print 'NO'
			elif ROOT.info == val:
					print 'YES'
					sys.exit(0)
			elif val < ROOT.info:
					self.query(ROOT.left, val)
			else: 
					self.query(ROOT.right, val)

		def deleteNode(self,val):
			ROOT = self.root # Not yet complete
      
		def Minimum(self,node):
			ROOT = node
			while ROOT != None:
					Val = ROOT.info
					ROOT = ROOT.left
			return Val

		def Maximum(self,node):
			ROOT = node
			while ROOT != None:
					Val = ROOT.info
					ROOT = ROOT.right
			return Val


		def SumPre(self,node):
			if node == None:
					return 0
			else:
					return node.info + self.SumPre(node.left) + self.SumPre(node.right)

		def SumDes(self,node):
			if node != None:
					node.info = self.SumPre(node) - node.info
					self.SumDes(node.left)
					self.SumDes(node.right)

		def ChangeTree(self,node):
			if node != None:
					node.info = self.Maximum(node)
					self.ChangeTree(node.left)
					self.ChangeTree(node.right)

		def DelAllNodeS(self,node):
			if node == None:
					return
			else:
					self.DelAllNodeS(node.left)
					self.DelAllNodeS(node.right)
					if node.left == None and node.right == None:
						print node.info
						node = None
                        
		def Klargest(self,node,k):
			if node != None:
					if k == 0:
						print node.info
						sys.exit(0)
					else:
						k = k -1 
						self.Klargest(node,k-1)
						self.Klargest(node,k-1)

		def Mirror(self,node):
			if node != None:
#          	       k = node.left
					node.left = self.Mirror(node.right)
					node.right = self.Mirror(node.left)

		def Child(self, node,ar):
			if node != None:
					if node.left == None and node.right == None:
						ar.append(node.info)
					self.Child(node.left,ar)
					self.Child(node.right,ar)
					return ar
            
		def Circumference(self,node):
			ROOT = node
			left = []
			right = []
			while ROOT != None:
					left.append(ROOT.info)
					ROOT = ROOT.left
			ROOT = node
			while ROOT != None:
					right.append(ROOT.info)
					ROOT = ROOT.right
			Child = self.Child(node,[])
			if left[-1] == Child[0]:
					CC = left[:-1] + Child
			else:
					CC = left + Child
			right.reverse()
			if CC[-1] == right[0]:
					CC = CC + right[1:]
			else:
					CC = CC + right
			print CC

		def Height(self,node):
			if node == None:
					return 0
			else:
					left = self.Height(node.left)
					right = self.Height(node.right)
					return 1+max(left,right)
                  
		def Diameter(self,node):
			if node ==  None:
					return 0
			else:
					Left = self.Height(node.left)
					Right = self.Height(node.right)
					return 1 + Left + Right
                  
		def print_tree_in(self,node):
			stack = []
			current = node
			while True:
				while current is not None:
					stack.append(current)
					current = current.left;
			if not stack:
				return
			current = stack.pop()
			print current.info
			while current.getRight is None and stack:
				current = stack.pop()
				print current.info
			current = current.right;

                 
tree = BinarySearchTree()     
arr = [8,3,1,6,4,7,10,14,13]
for i in arr:
      root = tree.create(i)
print '____Breadth-First Traversal____'
tree.bft()
print '____Inorder Traversal____'
tree.inorder(tree.root) 
print '____Preorder Traversal____'
tree.preorder(tree.root)
print 'Postorder Traversal'
tree.postorder(tree.root)
print('____Query in a BST____')
tree.query(root,30)
print('____min and max of a BST____')
print(tree.Minimum(tree.root))
print(tree.Maximum(tree.root))
print('____Sum of All Elements____')
total = tree.SumPre(tree.root)
print total
print ('____Replace Sum of Descendants____')
#tree.SumDes(tree.root)
#tree.preorder(tree.root)
print ('____Replace by Max of Subtree____')
#tree.ChangeTree(tree.root)
#tree.preorder(tree.root)
print('____Constructing the same BST from post order traversal of the first tree____')
tree1 = BinarySearchTree()
ARR = [1,4,7,6,3,13,14,10,8]
ARR.reverse()
for i in ARR:
      tree1.create(i)
print ('____visualise the tree____')
tree1.bft()
print('____Child____')
print (tree.Child(tree.root,[]))
print ('____Circumference____')
tree.Circumference(tree.root)
tree.newOrdering()
print ('___Common Ancestor___')
print ('____Height___')
print (tree.Height(tree.root))
print ('____Diameter____')
print(tree.Diameter(tree.root))
print('____PreorderIterative____')
tree.print_tree_in(tree.root)
