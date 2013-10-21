def binary_search(a, x):
    a.sort()
    lo = 0;
    hi = len(a);
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1

m = input()
n = input()
ar = [int(i) for i in raw_input().strip().split()]
K = binary_search(ar,n)
if K != -1:
    print('Found')
else:
    print ('Not Found')
