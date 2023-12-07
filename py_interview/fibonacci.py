"""
The type 1 solution: + uses for, - does not use python specifics that much

def fibonacci(n):
	arr = [0] * n 
	arr[1] = 1
	for i in range (2,n):
		arr[i] = arr[i-2] + arr[i-1]
	return arr"""



def fibonacci(n):
	arr = [0, 1]
	while len(arr) < n:
		next_var = arr[-1] + arr[-2]
		arr.append(next_var)

	return arr

res = fibonacci(5)
print(res)