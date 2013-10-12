from fractions import gcd
# SPOJ Problem
def ENIGMATH(ar):
    for i in range(len(ar)):
        Nos = ar[i].split();
        A = int(Nos[0]);
        B = int(Nos[1]);
        K = gcd(A,B);
        print B/K, A/K
m = input()
ar = [];
for i in range(m):
    ar.append(raw_input());
ENIGMATH(ar)
