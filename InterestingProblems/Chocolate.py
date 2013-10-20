def Chocolate(ar):
    for i in range(len(ar)):
        Input = [int(i) for i in ar[i].strip().split()]
        if Input[0] < Input [1]:
            print '0'
        else: 
            Exchange = Input[2]
            Sum = 0
            D = 1
            Wrappers = Input[0] / Input[1]
            while D > 0:
                D , R = Wrappers / Exchange, Wrappers % Exchange
                Sum = Sum + D
                Wrappers = D + R
            print Input[0]/Input[1]+ Sum

               
m = input()
I = 0 
ar = []
while I < m:
        K = raw_input()
        if K:
            ar.append(K)
            I += 1
Chocolate(ar)
