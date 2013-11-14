def Triplets():
        m = input()
        A = [int(i) for i in raw_input().strip().split()]
        B = [0]
        C = []
        I = 1
        while I <len(A):
            Min = min(A[:I])
            B.append(A[:I].index(Min))
            I += 1
        I = 0 
        while I < len(A) - 1:
            Max = max(A[I:])
            C.append(I + A[I:].index(Max))
            I += 1
        K = 1
        count = 0
        while K < len(A) - 1:
            if B[K] < K and C[K] > K:
                count += 1
            K += 1
        print count
                


if __name__ == '__main__':
    Triplets()