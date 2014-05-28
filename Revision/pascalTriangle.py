class Solution:
	def generate(self, numRows):
		ROWS = []
		if numRows == 1:
			ROWS.append([1])
			return ROWS
		else:
			I = 1
			ROWS.append([1])
			while I < numRows:
				temp = []
				LAST = ROWS[-1]
				temp.append(LAST[0])
				for i in range(len(LAST) - 1):
					temp.append(LAST[i] + LAST[i+1])
				temp.append(1)
				ROWS.append(temp)
				I += 1
			return ROWS
			
	def getRow(self, rowIndex):
		if rowIndex == 1:
			return [1]
		else:
			I = 1
			ROWS = [1]
			while I < rowIndex:
				temp = []
				temp.append(ROWS[0])
				for i in range(len(ROWS) - 1):
					temp.append(ROWS[i] + ROWS[i+1])
				temp.append(1)
				ROWS = temp
				I += 1
			return ROWS
					

if __name__ == '__main__':
	S = Solution()
	print S.generate(1)
	print S.getRow(4)
