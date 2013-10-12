import numpy
import sys
import math
from numpy import matrix as MA
def DIV15(ar):
    for i in range(len(ar)):
        No = str(ar[i]);
        Label = []
        for COUNT in range(10):
            Label.append(0)
        for IDX in range(len(No)):
            Label[int(No[IDX])%10]  = Label[int(No[IDX])%10] + 1 
        NewNumber = []
        Label.reverse()
        for K in range(len(Label)):
            if Label[K] != 0:
                NewNumber.append(9 - K)
        Number = "";
        for i in NewNumber:
            Number = Number + str(i)
        OUTPUT = int(Number) - int(Number)%15;
        if int(Number)/15 ==  0 and int(Number)%15 >0 :
            print 'IMPOSSIBLE'
        else:
            print int(Number) - int(Number)%15;
m = input()
ar = [];
i = 0;
while i < m:
    K = raw_input();
    if K:
        ar.append(K.strip());
        i += 1;
DIV15(ar)




