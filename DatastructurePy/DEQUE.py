"""
DEQUE
Author: ankush2@ualberta.ca
_________________________________________________________________________________________________-

 Simple Implementation of Deque. Deque is a datastructure that can be used both as a stack as
well as a queue. It does not have any FIFO or LIFO. New elements can be added and deleted from both ends.
A simple application of a palindrome checker is built using Deque
"""


class Deque:
    def __init__(self):
        self.data = []
        
    def Addrear(self,data):
        return(self.data.append(data))
    
    def AddFront(self,data):
        return(self.data.insert(0,data))
    
    def removeFront(self):
        return (self.data.pop(0))
    
    def removeEnd(self):
        return (self.data.pop())

    def size(self):
        return (len(self.data))

#D = Deque()
#D.Addrear(1)
#D.Addrear(1)
#D.AddFront(2)
#D.AddFront(10)
##D.removeFront()
#D.removeEnd()
#D.removeFront()
#D.removeFront()

            

from Deque import Deque

def checkpalindrome(ar):
    D = Deque()
    for i in ar:
        D.Addrear(i)
    Pal = 'TRUE'
    while D.size() > 1 and Pal == 'TRUE': 
        print D.size()
        E1 = D.removeFront()
        E2 = D.removeEnd()
        if E1 == E2:
            Pal = 'TRUE'
        else: 
            Pal = 'FALSE'
    print Pal
    
    
K = list(str(raw_input('Enter the string:    ')))
checkpalindrome(K)
