"""  
Python program to Delete a node from SLL, in which the last node points to the middle node( in case of even no of nodes, it points to the first middle node) and update the SLL.

 Author: ankush2@ualberta.ca

"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return (str(self.data))

class LinkedList:
    def __init__(self):
        self.root = None

    def AddNode(self,val):
        NewValue = Node(val)
        if self.root == None:
            self.root = NewValue
        else:
            NewValue.next = self.root
            self.root = NewValue

    def size(self):
        ROOT = self.root
        COUNT = 0
        while ROOT != None:
            COUNT += 1
            ROOT = ROOT.next
        return COUNT

    

A = LinkedList()
A.AddNode(1)
A.AddNode(2)
A.AddNode(20)
A.AddNode(10)
print (A.size())
