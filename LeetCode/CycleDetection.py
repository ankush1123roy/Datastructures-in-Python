"""LeetCode: Cycle DetectionI
             Cycle DetectionII

   Author: ankush2@ualberta.ca
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.root = None

    def Insert(self,val):
        NewNode = Node(val)
        if self.root == None:
            self.root = NewNode
        else:
            NewNode.next = self.root
            self.root = NewNode
        return self.root

    def Print(self,Node):
        ROOT = Node
        while ROOT != None:
            print ROOT.data
            ROOT = ROOT.next
            

    def DetectCycle(self,Node):
        tortoise = Node
        hare = Node
        Found = 'FALSE'
        while  Found == 'FALSE':
            if hare == None:
                print 'DeadEnd'
                Found = 'TRUE'
            hare = hare.next
            if hare == None:
                print 'DeadEnd'
                Found = 'TRUE'
            hare = hare.next
            tortoise = tortoise.next
            if tortoise == hare:
                print tortoise
                print tortoise.data
                Found = 'TRUE'


            
A = SLL()
A1 = A.Insert(1)
A2 = A.Insert(3)
A3 = A.Insert(6)
A4 = A.Insert(7)
A1.next = A4
A.DetectCycle(A1)

