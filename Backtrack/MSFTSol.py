class solutionMSFT():
	
	def removeDup(self, str):
		STR = list(str)
		dict = {}
		I = 0 
		L = len(STR) - 1
		
		while I <= L:
			if STR[I] not in dict:
				dict[STR[I]] = ''
				I += 1
			else:
				STR[I], STR[L] = STR[L], STR[I]
				L = L - 1
		for i in range(len(str)  - I):
			STR.pop()
		print ''.join(STR)

	'''def searchRotated(self, arr, target):
		lo = 0 
		hi = len(arr) - 1
		while lo <= hi:
			mid = (lo + hi) / 2
			if arr[mid] == target:
				return mid
			elif target < arr[hi] and target > arr[mid]:
				lo = mid + 1
			elif target > arr[lo] and target < arr[mid]:
				hi = mid - 1
			elif 
	'''
	def missingEle(self, array):
		I  = 0 
		while I < len(array) - 1:
			if array[I+1] - array[I] != 1:
				print array[I] + 1
				break
			I += 1
		print len(array) + 1
	
	def generateEle(self, array, temp, index, sol):
		'''
		Given a set. Generate all sub sets where an element can occur as 
		many times as possible from that set
		'''
		if index == 0:
			sol.append(temp)
			return
		else:
			for i in array:
				self.generateEle(array, temp + [i], index - 1, sol)
		return sol
		
	def grayCodes(self, index, final, temp):
		print ''.join(temp)
		import pdb;pdb.set_trace()
		temp[index - 1] = '1'
		self.grayCodes(index - 1, final, temp)
		self.grayCodes(index - 1, final, temp)
				
			
			
			
	
if __name__ == '__main__':
	S = solutionMSFT()
	S.removeDup('AaAa')
	index = 3
	temp = []
	print S.generateEle([1,2,3], temp, index, sol = [])
	S.grayCodes(4, 4, ['0','0','0','0'])
				
