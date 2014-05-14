def subSetSum(A, sum, k):
	if sum == k:
		print True
		return
	elif sum > k:
		return 
	else:
		for i in range(len(A)):
			A = A[i:]
			return subSetSum(A[1:], sum + A[0], k) or subSetSum(A[1:], sum, k)


def subSetSum1(A, temp, k):
	if sum(temp) == k:
		print temp
		return
	elif sum(temp) > k:
		return 
	else:
		for i in range(len(A)):
			return subSetSum1(A[1:], temp + [A[0]], k) or subSetSum1(A[1:], temp, k)

if __name__ == '__main__':
	A = [4,5,8,2,3,1]
	k = 10
	sol = 0
	temp = []
	subSetSum(A, 0, k)
	subSetSum1(A, temp, k)
