class Solution():
	
	def singleNumber1(self, A):
		if len(A) == 0:
			return 0 
		elif len(A) == 1:
			return A[0]
		else:
			xorFull = A[0]
			for  i in range(1,len(A)):
				xorFull = xorFull ^ A[i]
			return xorFull

