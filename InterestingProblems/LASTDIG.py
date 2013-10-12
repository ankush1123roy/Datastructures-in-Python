def LASTDIG(ar):
    for i in range(len(ar)):
        Nos = ar[i].split();
        b = int(Nos[1])
        L = int(Nos[0][-1]);
        C4 = b%4;
        C2 = b%2;
        C3 = b%3;
        if  b == 0:
            print '1'
        elif L == 0 and b!=0:
            print '0'
        elif C4 == 0:
            V = str(L**4);
            print int(V[-1])
        elif C3 == 0:
            V = str(L**3);
            print int(V[-1])
        elif C2 == 0 and C4 !=0:
            V = str(L**2);
            print int(V[-1])
        elif C4 ==1:
            print L
m = input()
I = 0;
ar = []
while I<m:
    K = raw_input()
    if K:
        ar.append(K)
    I +=1
LASTDIG(ar);


