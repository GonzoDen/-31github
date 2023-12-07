def is_palindrome(s):
	s2 = s[::-1]
	if s2 == s:
		return True
	else:
		return False