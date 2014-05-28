class Solution():
	
	def isPalindrome(self, s):
		s = list(s)
		new_letters = []
		for i in s:
			if  65<= i <= 90 or 97 <= i <= 122 or 48 <= i <= 57:
				new_letters.append(i)
		lo = 0 
		hi = len(new_letters) - 1
		while lo < hi:
			if s[lo] != s[hi]:
				return False
			lo += 1
			hi -= 1
		return True
