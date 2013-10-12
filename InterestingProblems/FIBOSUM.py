def FIBOSUM(ar):
    for i in range(len(ar)):
        Sum = 0 ;
        Nos = ar[i].split();
        Seq = Fibonacci(int(Nos[-1]))
#        import pdb;pdb.set_trace()
        for i in range(int(Nos[0]), int(Nos[1])+ 1):
            Sum = Sum + Seq[i]
        print Sum
        


def Fibonacci(ar):
    Fibonacci = []
    for i in range(ar+1):
        if i == 1 or i ==0:
            Fibonacci.append(1)
        else:
            Fibonacci.append(Fibonacci[i-1] + Fibonacci[i-2])
    return Fibonacci







m = input()
I = 0;
ar = []
while I < m:
    K = raw_input();
    if K:
        ar.append(K);
    I +=1;
FIBOSUM(ar)
