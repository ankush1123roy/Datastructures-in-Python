def SingleNumber():
    m = input()
    for i in range(m):
        Ar = [int(i) for i in raw_input().strip().split()]
        XORAll = Ar[1]
        for i in range(1,len(Ar)):
            XORAll = Ar[i] ^ XORAll
        I = 0
        while I < len(Ar):
            if Ar[I] ^ XORAll == 0:
                print Ar[I]
                break
            I += 1
if __name__ == '__main__':
    SingleNumber()