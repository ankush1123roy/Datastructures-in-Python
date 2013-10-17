def NSTEPS(ar):
    for i in range(len(ar)):
        CO = [int(i) for i in ar[i].strip().split()]
        if CO[0] - CO[1] == 2 or CO[0] == CO[1]:
            if CO[0] % 2 == 0:
                if CO[0] == CO[1]:
                    print CO[0] * 2
                else:
                    print (CO[0] - 1) * 2
            else:
                if CO[0] == CO[1]:
                    print (CO[0] - 1) * 2 + 1
                else:
                    print  (CO[0] - 1) * 2 -1

        else:
            print 'No Number'


m = input()
ar = []
I = 0
while I < m:
    K = raw_input()
    if K:
        ar.append(K)
        I = I + 1
NSTEPS(ar)
