def ants(ar,n):
    for i in range(len(ar)):
        Positions = [int(i) for i in ar[i].split()]
        Min = 0;
        Max = 0;
        for IDX in range(len(Positions)):
            v1 = min(abs(Positions[IDX] - n), Positions[IDX])
            if v1  > Min:
                Min = v1
            v1 = max(abs(Positions[IDX] -n) , Positions[IDX]);
            if v1 > Max:
                Max = v1;
        print Min,Max
m = input()
n = input()
ar = [];
for i in range(m):
    ar.append(raw_input());

ants(ar,n)
