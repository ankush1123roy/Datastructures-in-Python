def FACT(ar):
    for i in ar:
        print factorial(i)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)







m = input()
I = 0 
ar = []
while I < m:
    K = int(raw_input())
    if K:
        ar.append(K)
        I +=1

FACT(ar)
