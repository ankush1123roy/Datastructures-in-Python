""" Linked List has next pointer and random pointer. We have to copy the linked list witthout using extra space.
    The only space that can be used is the new Linked List that is created. Random Pointers should be same as 
    that of the original Linked List.

Author: ankush2@ualberta.ca
"""


import random 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None
        
    def __str__(self):
        return (str(self.data))


class LinkedList:
    def __init__(self):
        self.root = None
        
    def isEMPTY(self):
        if self.root == None:
            return 'TRUE'
        else:
            return 'FALSE'

    def AddNode(self,data):
        NewNode = Node(data)
        if self.root == None:
            self.root = Node(data)
        else: 
            NewNode.next = self.root
            self.root = NewNode

    def size(self):
        ROOT = self.root
        COUNT = 0
        while ROOT != None:
            COUNT += 1
            ROOT = ROOT.next
        return COUNT

    def RandomAllocation(self,param):
        ROOT = self.root
        while ROOT != None:
            T = self.root
            No = int(param * random.random())  
            for i in range(No):
                T = T.next
            ROOT.random = T
            ROOT = ROOT.next

    def duplicate(self):
        ROOT = self.root
        while ROOT != None:
            NewNode = Node(ROOT.data)
            Current = ROOT.next
            CurrentR = ROOT.random 
            ROOT.next = NewNode
            NewNode.next = Current
            NewNode.random = CurrentR
            ROOT = Current

    def FinalList(self,size):
        self.root = self.root.next
        ROOT = self.root
        I = 0
        while I < size/2 - 1:
            ROOT.next = ROOT.next.next
            I += 1
            



A = LinkedList()
print(A.isEMPTY())
for i in range(1,10):
    A.AddNode(i)

print(A.size())
A.RandomAllocation(A.size())   
A.duplicate()      
print(A.size())
A.FinalList(A.size())
print(A.size())
