class atoi:

    def INT_MIN(self,M):
        M = list(M)
        ar = []
        ar.append('-')
        for i in range(len(M)):
            if ord(M[i]) <= 57 and ord(M[i]) >= 48:
                ar.append(M[i])
            else:
                break
        
        return ''.join(ar)

    def INT_MAX(self,M):
        ar = []
        for i in range(len(M)):
            if ord(M[i]) <= 57 and ord(M[i]) >= 48:
                ar.append(M[i])
            else:
                break
                
        return ''.join(ar)
        
A = atoi()
m = input()
for i in range(m):
    Ar = str(raw_input().strip())
    print A.INT_MIN(Ar)
    print A.INT_MAX(Ar)