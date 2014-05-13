import sys
sys.setrecursionlimit(100000)
import time

'''
A Rat starts from (0,0) in a maze and traverses all the way to reach
the end of the board (m + 1,n + 1)

Possible Questions:
-------------------

1. No of Paths (Mathematically)
2. No of paths (Recursively) {Remember the 
original naive recursion would be exponential}
3. Print the paths
4. No of paths if some location blocked
5. No of paths (Recursively using DP)
'''

def routeInMaze(startx, starty, M , N, temp, blockX, blockY):
	if startx in blockX and starty in blockY:
		return
	else:
		if startx == M:
			for i in range(starty, N + 1):
				temp = temp +  [(N,i)]
			print temp
			print '\n'
		elif starty == N:
			for i in range(startx, M + 1):
				temp = temp + [(i,M)]
			print temp
			print '\n'
		else:
			routeInMaze(startx + 1, starty, M , N, temp + [(startx,starty)], blockX, blockY)
			routeInMaze(startx, starty + 1, M , N, temp + [(startx,starty)], blockX, blockY)

def noPaths(startx, starty, M, N):
	if startx == M and starty == N:
		return 1 
	elif startx > M or starty > N:
		return 0
	else:
		return noPaths(startx + 1, starty, M, N) + noPaths(startx, starty+1, M, N)
		
def noPathsBlock(startx, starty, M, N, blockX, blockY):
	if startx == M and starty == N:
		return 1 
	elif startx > M or starty > N:
		return 0
	elif startx in blockX and starty in blockY:
		return 0
	else:
		return noPathsBlock(startx + 1, starty, M, N, blockX, blockY) + noPathsBlock(startx, starty+1, M, N, blockX, blockY)

def noPathsDP( M, N, blockX, blockY):
	PathCount =  [[0 for i in range(N+1)] for j in range(M+1)]
	for i in range(1, N+1):
		PathCount[0][i] = 1
	for j in range(1, M+1):
		PathCount[j][0] = 1
	for i in range(1,M+1):
		for j in range(1,N+1):
			if i in blockX and j in blockY:
				pass
			else:
				PathCount[i][j] = PathCount[i-1][j] + PathCount[i][j-1]
	print PathCount[-1][-1]

if __name__ == '__main__':
	startx, starty = 0, 0
	M, N = 2, 2
	blockx = [1]
	blocky = [1]
	print noPathsBlock(startx, starty, M, N, blockx, blocky)
	noPathsDP( M, N, blockx, blocky)
	print  noPaths(startx, starty, M, N)
	temp = []
	routeInMaze(startx, starty, M , N, temp, blockx, blocky)

