def SumlessthanT(ar,K):
    ar.sort()
    I = 0 
    L = len(ar) - 1
    results = 0 
    LNum = ar[0]
    HNum = ar[-1]
    if LNum + HNum < K:
        results = 1
    while I <=  L:
        if ar[I] + ar[L]  < K and (LNum != ar[I] or HNum != ar[L]):
            results += 1
            LNum = ar[I] 
            HNum = ar[L]
            I += 1
        else:
            L -= 1
    print results
            
m = input()
K = input()
m = [int(i) for i in raw_input().strip().split()]
SumlessthanT(m,K)
