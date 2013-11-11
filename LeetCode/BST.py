class Node:

    def __init__(self,data):

        self.data = data
        self.right = None
        self.left = None
        self.level = None

    def __str__(self):
        return str(self.data)

class BST:
    
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            Present = self.root
            while 1:
                if val < Present.data:
                    if Present.left:
                        Present = Present.left
                    else:
                        Present.left = Node(val)
                        break
                elif val > Present.data:
                    if Present.right:
                        Present = Present.right
                    else:
                        Present.right = Node(val)
                        break
                else:
                    break
        return self.root
        


A = BST()
A1 = A.insert(3)
A2  = A.insert(2)
import pdb;pdb.set_trace()
A.insert(1)
A.insert(10)