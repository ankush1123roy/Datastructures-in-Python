'''
Trie
Author: ankush2@ualberta.ca
Node defined by three entries:

val = character
ref = Pointers to the rest of the nodes
eof = To indicate the end of word
'''
class Node():
	
	def  __init__(self, data, eof):
		self.val = data
		self.ref = {}
		self.eof = eof

class trie():
	
	def __init__(self):
		self.start = {}
		
	def insert(self, word):
		if word[0] not in self.start:
			self.start[word[0]] = Node(word[0], False)
		I = 0
		ROOT = self.start[word[0]]
		while I < len(word) - 1:
			if word[I+1] not in ROOT.ref:
				ROOT.ref[word[I+1]] = Node(word[I+1],False)
			ROOT = ROOT.ref[word[I+1]]
			I += 1
		ROOT.eof = True
	
	def predictWord(self, word):
		START_NODE = word[0]
		ROOT_WORD = [] 
		if START_NODE not in self.start:
			print 'No words starting with ', START_NODE
			return 
		else:
			ROOT = self.start[START_NODE]
			I = 0 
			while I < len(word) - 1:
				ROOT_WORD.append(ROOT.val)
				if word[I+1] in ROOT.ref:
					ROOT = ROOT.ref[word[I+1]]
				else:
					print 'No matching word found'
					return
				I += 1
			ROOT_WORD = ''.join(ROOT_WORD)
			ALL = self.generateAllpaths(ROOT, tmp = [], sol = [])
			for i in range(len(ALL)):
				ALL[i] = ROOT_WORD + ALL[i]
			return ALL
		
	def generateAllpaths(self, Node, tmp, sol):
		if len(Node.ref) >= 0:
			tmp = tmp + [Node.val]
			for i in Node.ref.keys():
				self.generateAllpaths(Node.ref[i], tmp , sol)
			if Node.eof == True:
				sol.append(''.join(tmp))
		return sol



if __name__ == '__main__':
	T = trie()
	A = ['Ankush','Amla','Bedwa']
	for i in A:
		T.insert(i)
	print T.predictWord('An')
