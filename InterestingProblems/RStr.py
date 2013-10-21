def RSTR(ar):
    ar = list(ar)
    L = len(ar)
    P1 = 0
    P2 = len(ar) - 1
    swap = 0
    while P1 <= P2:
        swap = ar[P2]
        ar[P2] = ar[P1]
        ar[P1] = swap
        P1 +=1
        P2 -=1
    print ''.join(ar)

ar = str(raw_input())
RSTR(ar)
