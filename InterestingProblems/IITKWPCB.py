from fractions import gcd
def IITKWPCB(ar):
    for i in range(len(ar)):
        No1 = ar[i];
        No2 = No1/2;
        I = 0;
#        import pdb;pdb.set_trace()
        while I >= -No2:
            if gcd(No1,No2+I) ==1:
                print No2+ I;
                break
            else:
                I = I - 1;

m = input()
#import pdb;pdb.set_trace()
I = 0;
ar = [];
while I<m:
    K = raw_input()
    if K:
        ar.append(int(K))
        I +=1

IITKWPCB(ar)
