
class Solution():
	
	def singleNumber(self, A):
		dict = {}
		for i in A:
			if i not in dict:
				dict[i] = 1
			else:
				dict[i] = dict[i] + 1
		keys = dict.keys()
		for i in keys:
			if dict[i] != 3:
				return i
