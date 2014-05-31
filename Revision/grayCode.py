class Solution:
	
	def grayCodes(self, noBits, temp, sol):
		if len(temp) == 2**noBits:
			return temp
		else:
			array = []
			for i in temp:
				array.append([0]+i)
			temp.reverse()
			for i in temp:
				array.append([1] + i)
			return self.grayCodes(noBits, array, sol)
				
if __name__ == '__main__':
	S = Solution()
	print S.grayCodes(3, temp = [[]], sol = [])
		
