from random import *  
from math import sqrt  
inside=0  
n=100000000000000000000000  
for i in range(0,n):  
    x=random()  
    y=random()  
    if sqrt(x*x+y*y)<=1:  
        inside+=1  
    pi=4*inside/float(n)
    print pi  
