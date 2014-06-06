class Solution():
	'''
	Manhattan Tourist 
	or max path with movement restricted to east and south
	'''
	def manhattanTourist(self, grid, m, n):
		dp = []
		for i in range(m):
			temp = [0 for i in range(n)]
			dp.append(temp)
		dp[0][0] = grid[0][0]
		for i in range(1, m):
			dp[i][0] = dp[i - 1][0] + grid[i][0]
		for j in range(1, n):
			dp[0][j] = dp[0][j-1] + grid[0][j]
		
		for i in range(1, m):
			for j in range(1, n):
				dp[i][j] = max(dp[i-1][j]+ grid[i][j], dp[i][j-1]+ grid[i][j]) 
		import pdb;pdb.set_trace()
		print dp[m - 1][n - 1]

if __name__ == '__main__':
	S = Solution()
	grid = [[1,2,3],[8,21,2],[3,7,8],[11,2,1]]
	m, n = 4, 3
	S.manhattanTourist(grid, m, n)
