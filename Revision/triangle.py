class Solution:
	
	def minimumTotal(self, triangle):
		I = len(triangle) - 2
		while I >= 0:
			for i in range(len(triangle[I])):
				triangle[I][i] = min(triangle[I][i] + triangle[I+1][i], triangle[I][i] + triangle[I + 1][i + 1])
			I -= 1
		return triangle[0][0]

if __name__ == '__main__':
	S = Solution()
	array = [[2],[3,4],[6,5,7],[4,1,8,3]]
	print S.minimumTotal(array)
			
