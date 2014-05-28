class Solution():
	
	def evalRPN(self, tokens):
		if len(tokens) == 1:
			return int(tokens[0])
		elif len(tokens) == 0:
			return 0
		else:
			OPERANDS = []
			OPERATORS = ['+', '-', '*', '/']
			for i in tokens:
					if i not in OPERATORS:
						OPERANDS.append(int(i))
					else:
						no1 = OPERANDS.pop()
						no2 = OPERANDS.pop()
						if i == '+':OPERANDS.append(self.add(no2, no1))
						elif i == '-':OPERANDS.append(self.sub(no1, no2))
						elif i == '*':OPERANDS.append(self.mul(no2, no1))
						else:OPERANDS.append(self.div(no2, no1))
			return OPERANDS[-1]
				
			
		
		
	def add(self, no1, no2):
		return no1 + no2
	
	def sub(self, no1, no2):
		return no1 - no2
	
	def mul(self, no1, no2):
		return no1*no2
	
	def div(self, no1, no2):
		return int(float(no1)/ float(no2))
		
if __name__ == '__main__':
	S = Solution()
	tokens = ["2", "1", "+", "3", "*"]
	print S.evalRPN(tokens)
