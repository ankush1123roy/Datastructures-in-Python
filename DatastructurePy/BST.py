'''
   Binary Search Tree
   No Duplicate Values are allowed in BST. So its an ordered BST
   ------------------
Author: ankush2@ualbertaa.ca  
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
      
      def Minimum(self):
            ROOT = self.root
            while ROOT != None:
                  Val = ROOT.info
                  ROOT = ROOT.left
            return Val

      def Maximum(self):
            ROOT = self.root
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

                  
tree = BinarySearchTree()     
arr = [8,3,1,6,4,7,10,14,13]
for i in arr:
      root = tree.create(i)
print 'Breadth-First Traversal'
tree.bft()
print 'Inorder Traversal'
tree.inorder(tree.root) 
print 'Preorder Traversal'
tree.preorder(tree.root)
print 'Postorder Traversal'
tree.postorder(tree.root)
tree.query(root,30) 
print(tree.Minimum())
print(tree.Maximum())
print('________Sum of All Elements____________')
#import pdb;pdb.set_trace()
total = tree.SumPre(tree.root)
print total
print ('_____Replace Sum of Descendants_________')
tree.SumDes(tree.root)
tree.preorder(tree.root)