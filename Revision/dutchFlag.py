import time
def dutchFlag(A):
	I = 0
	lo = 0 
	hi = len(A) - 1 
	while I <= hi:
		if A[I] == 0:
			A[I], A[lo] = A[lo], A[I]
			lo += 1
			I += 1
		elif A[I] == 2:
			A[I], A[hi] = A[hi], A[I]
			hi -= 1
		else:
			I += 1
	return A

def dutchFlag1(A):
	lo = 0 
	hi = len(A) - 1
	while lo < hi:
		if A[lo] > 0:
			A[lo], A[hi] = A[hi], A[lo]
			hi -= 1
		else:
			lo += 1
	lo = 0
	hi = len(A) - 1 
	while lo < hi:
		if A[lo] == 2:
			A[lo], A[hi] = A[hi], A[lo]
			hi -= 1
		else:
			lo += 1
	return A

