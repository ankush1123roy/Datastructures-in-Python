from copy import deepcopy
def BITONIC(ar):
    MaxCount = 0 
    i, idx  = 0, 0 
    P = 0
    NewCount = 0
    New = [0]
    while idx < len(ar) - 1: 
        if ar[idx+1] >= ar[idx]:
            New.append(1)
        else:
            New.append(0)
        idx +=1
    
    while i < len(ar) - 1:
#        import pdb;pdb.set_trace()
        if New[i]  == 1:
            NewCount, P = 0, i 
            Pval = deepcopy(P)
            while P < len(ar) - 1:
                if New[P+1] <= New[P]:
                    NewCount += 1
                else:
                    break
                P += 1
        if P == 0 :
            i = i + 1
        else:
            i = P
        if NewCount > MaxCount: 
            MaxCount = NewCount
            Pval = deepcopy(P) - NewCount 

    import pdb;pdb.set_trace()        
    if MaxCount+1 == len(ar) - 1:
        print 'Monotonic'
    elif MaxCount == 0:
        print 'Monotonic'
    elif len(ar) - Pval == MaxCount:
        print 'Negative Depression'
    else: 
        print Pval-1, MaxCount+1

ar = [int(i) for  i in raw_input().strip().split()]
BITONIC(ar)
