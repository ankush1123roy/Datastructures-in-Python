import random

def Children(ar,k):
    ar.sort()
    Min = ar[-1]
    l = 0
    while (l+k) < len(ar):
        Dif  =  ar[l+k-1] - ar[l]
        if Dif < Min:
            Min = Dif
        l +=1
    print Min


m = input()
n = input()
ar = []
I = 0 
for i in range(m):
    ar.append(int(raw_input()))
Children(ar,n)
