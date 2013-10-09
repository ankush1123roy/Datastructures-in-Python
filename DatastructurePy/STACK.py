""" Class for Stack and QUEUE. The stack implementation assumes that stacks operate 
in contiguous pieces of memory and not random allocation of memory in RAM which can be
seen in the case of Linked List 

    Author: ankush2@ualberta.ca
"""


class STACK:
    def __init__(self):
        self.data= []
    def push(self,val):
        return(self.data.append(val))
    def pop(self):
        print(self.data.pop())

class QUEUE:
    def __init__(self):
        self.data = []
    def enqueue(self,val):
        return (self.data.append(val))
    def dequeue(self):
        print self.data[0]
        del self.data[0]


S = STACK()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.pop()
S.pop()


Q = QUEUE()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.dequeue()
