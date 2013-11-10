""" LeetCode: Reorder Single Linked List
L0 -> Ln -> L1-> Ln-1 -> ...

Author: ankush2@ualberta.ca"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.root = None

    def create(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            NewNode = Node(val)
            NewNode.next = self.root
            self.root = NewNode
        return self.root

    def isEmpty(self):
        if self.root == None:
            print 'YES'
            
    def NoElements(self):
        ROOT = self.root
        count = 0
        while ROOT != None:
            count = count + 1
            ROOT = ROOT.next
        return count

    def Reorder(self,Elements):
        Start = 0
        End = Elements - 1 
        L, T = self.root, self.root
        while Start <= End:
            NextEl = L.next
            K = Start
            while K < End:
                T = T.next
                K += 1
            End = End - 1
            Start = Start + 1
            L.next = T
            L,T.next = NextEl, NextEl
            T = L
        T.next = None
        return self.root
        
    def Print(self,node):
        ROOT = self.root
        while ROOT != None:
            print ROOT.data
            ROOT = ROOT.next
            
A = SLL()
AA = A.create(4)
AA = A.create(2)
AA = A.create(3)
AA = A.create(1)
AA = A.create(7)
AA = A.create(9)
A.Print(AA)
EL = A.NoElements()
VAL = A.Reorder(EL)
import pdb;pdb.set_trace()
A.Print(VAL)            
        