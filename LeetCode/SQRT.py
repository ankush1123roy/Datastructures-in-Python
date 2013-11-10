def SQRT():
    m = input()
    Eps = 0.00000001  # Set it according to precision
    for i in range(m):
        Number = int(raw_input())
        low = 0
        high = Number
        while 1:
            mid = (low + high)/float(2)
            if mid**2<Number+Eps and  mid**2 > Number - Eps:
                print mid
                break
            elif mid**2 < Number - Eps:
                low = mid
            else:
                high = mid

if __name__ == '__main__':
    SQRT()