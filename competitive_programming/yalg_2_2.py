import math

s = input().strip()

n = len(s)
p = 10**9 + 7
x_ = 257
h = [0] * (n+1)
x = [0] * (n+1)
x[0] = 1
s = ' ' + s

for i in range(1, n+1):
	h[i] = (h[i-1]*x_ + ord(s[i])) % p
	x[i] = (x[i-1]*x_) % p

def is_equal (slen,from1, from2):
	return (
		(h[from1 + slen] + h[from2] * x[slen]) % p == 
		(h[from2 + slen] + h[from1] * x[slen]) % p
	)

temp = n - 1
answer = 0

for i in range(n):
	l = temp 
	a = 0
	b = n - temp
	result = is_equal(l, a, b)
	if not result:
		temp -= 1
	else:
		k = n - temp
		print(k)
		break