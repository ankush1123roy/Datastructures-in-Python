class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return (str(self.data))

class LinkedList:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        if self.root == None:
            return 'TRUE'
        else:
            return 'FALSE'
    
    def AddNode(self,val):
        NewNode = Node(val);
        if self.root == None:
            self.root = NewNode
        else:
            NewNode.next = self.root
            self.root = NewNode
        return self.root

    def size(self):
        count = 0
        ROOT = self.root
        while  ROOT !=None:
            if ROOT:
                count = count + 1
                ROOT = ROOT.next
        return count
    
    def search(self,val):
        OCC = 'FALSE'
        ROOT = self.root
        while ROOT != None and OCC == 'FALSE':
            if ROOT.data == val:
                OCC = 'TRUE'
            else:
                ROOT = ROOT.next
        return OCC

    def delete(self,val):
        OCC = 'FALSE'
        ROOT = self.root
        if ROOT.data == val:
            self.root = ROOT.next
        else:
            while ROOT != None and OCC == 'FALSE':
                if ROOT.data == val:
                    OCC = 'TRUE'
                    current.next = ROOT.next
                else:
                    current = ROOT
                    ROOT = ROOT.next
    
    def traversal(self,i):
        ROOT = self.root
        K = 0
        while K < i:
            ROOT = ROOT.next
            K += 1
        return ROOT
    
    def reverse(self):
        LAST = None
        ROOT = self.root
        if self.root == None:
            return 'No Element in Linked List'
        while ROOT != None:
                NEXT = ROOT.next
                ROOT.next = LAST
                LAST = ROOT
                ROOT    = NEXT
        return LAST
                
    def Pprint(self,node):
        while node != None:
            print node.data
            node = node.next

    def swap(self):
        ROOT = self.root
        FIRST = self.root.next
        while ROOT != None:
            CURRENT = ROOT
            SWAP = ROOT.next
            SWAP.next = CURRENT
            CURRENT.next = CURRENT.next.next.next
            if ROOT.next.next != None :
                ROOT = ROOT.next.next
        self.root = FIRST
            
A = LinkedList()
print(A.isEmpty())
A1= A.AddNode(3)
A2 = A.AddNode(1)
A3 = A.AddNode(2)
A4 = A.AddNode(4)
A5 = A.AddNode(5)
REVERSE = A.reverse()
A.Pprint(REVERSE)
import pdb;pdb.set_trace()
print 'K'
