class Solution():
	
	def reverseWords(self, s):
		if len(s) > 0:
			s = list(s)
			start = 0 
			end = len(s) - 1
			while start < end:
				s[start], s[end] = s[end], s[start]
				start += 1
				end -= 1
			return ''.join(s)

	def reverseWordsPY(self, s):
		if len(s) > 0:
			s = list(s)
			s.reverse()
			return ''.join(s)
		
		
if __name__ == '__main__':
	S = Solution()
	print S.reverseWords('the sky is blue')
	print S.reverseWordsPY('the sky is blue')
