def ADDREV(ar):
    for i in range(len(ar)):
        Number = ar[i].split();
        N1 = removeZero(str(Number[0]))
        N2 = removeZero(str(Number[1]))
        N1 = ''.join(N1);
        N2 = ''.join(N2);
        SUM = removeZero(str(int(N1) + int(N2)))
        IntSum = ''.join(SUM);
        print int(IntSum)
        
def removeZero(No):
    No = list(No);
    for i in range(len(No)):
        if No[0] == '0':
            No.remove('0')
        else: 
            break
    No.reverse()
    for i in range(len(No)):
        if No[0] == '0':
            No.remove('0')
        else:
            break
    return No
        
m = input()
ar = [];
i = 0
while i < m:
    K = raw_input();
    if K: 
        ar.append(K)
        i = i+ 1
ADDREV(ar)
