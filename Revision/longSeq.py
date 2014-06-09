def longestSeq(A):
	SOL = []
	for i in range(len(A)):
		maxSeq = 0 
		for j in range(i):
			if A[j] < A[i]:
				if SOL[j] > maxSeq:
					maxSeq = SOL[j]
		SOL.append(maxSeq + 1)
	print SOL


if __name__ == '__main__':
	A = [2, 6, 3, 4, 1, 2, 9, 5, 8]
	longestSeq(A)
