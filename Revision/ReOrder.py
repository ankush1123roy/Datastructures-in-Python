from LL import *

class Solution:
	
	def Length(self, node):
		if node == None:
			return 0
		else:
			return 1 + self.Length(node.next)
	
	def reorderList(self, node):
		ROOT = node
		globalRoot = node
		Length = self.Length(node)
		I = 0 
		if Length % 2 == 0:
			while I < Length/2 - 1:
				ROOT = ROOT.next
				I += 1
		else:
			while I < Length/2:
				ROOT = ROOT.next
				I += 1
		splitNode = ROOT.next
		ROOT.next = None
		splitList = self.reverse(splitNode)
		while node != None and splitList != None:
			temp = node
			NEXT1 = node.next
			temp1 = splitList
			NEXT2 = splitList.next
			node.next = splitList
			splitList.next = NEXT1
			node = NEXT1
			splitList = NEXT2
		return globalRoot
			
	def reverse(self, node):
		ROOT = node
		LAST = None
		while ROOT != None:
			NEXT = ROOT.next
			ROOT.next = LAST
			LAST = ROOT
			ROOT = NEXT
		return LAST
	


if __name__ == '__main__':
	S = Solution()
	A = [4,3,2,1]
	L = LL()
	for i in A:
		T = L.Insert(i)
	R  =  S.reorderList(T)
	import pdb;pdb.set_trace()
	L.Print(R)
