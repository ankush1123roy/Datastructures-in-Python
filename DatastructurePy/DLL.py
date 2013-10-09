""" Doubly Linked List 
References have three fields, 1) Data Field
2) Reference to the next Object
3) Reference to the Previous Field

Methods Described here are 
AddNode()
isEmpty()
size()
search()
Remove()

Author: ankush2@ualberta.ca

"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
    def __str__(self):
        return(str(self.data))

class DLL:
    def __init__(self):
        self.root = None
        
    def isEmpty(self):
        if self.root == None:
            return 'YES'
        else:
            return 'NO'
        
        
    def AddNode(self,data):
        NewNode = Node(data)
        if self.root == None:
            self.root = NewNode
        else: 
            self.root.prev = NewNode
            NewNode.next = self.root
            self.root = NewNode

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

    def remove(self, val):
        VAL = 'FALSE'
        ROOT = self.root
        if ROOT.data == val:
            self.root = ROOT.next
        else:
            while ROOT != None and VAL == 'FALSE':
                if ROOT.data == val:
                    VAL = 'TRUE'
                    current.next = ROOT.next
                else:
                    current = ROOT
                    ROOT = ROOT.next
                ROOT.prev = current


A = DLL()
print (A.isEmpty())
A.AddNode(1)
A.AddNode(2)
A.AddNode(3)
print(A.size())
A.remove(2)
print(A.size())
