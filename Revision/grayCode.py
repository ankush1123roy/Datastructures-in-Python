class Solution:
	
	def grayCodes(self, noBits, temp):
		if len(temp) == 2**noBits:
			return temp
		else:
			array = []
			for i in temp:
				array.append([0]+i)
			temp.reverse()
			for i in temp:
				array.append([1] + i)
			return self.grayCodes(noBits, array)
				
if __name__ == '__main__':
	S = Solution()
	LL =  S.grayCodes(3, temp = [[]])
	import pdb;pdb.set_trace()
		
