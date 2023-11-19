def merge (a_l, a_r, b_l, b_r):
	f = []
	
	while (b_l < b_r) and (a_l < a_r): #removed '<=' to avoid issues with empty arrays
		if a[a_l] <= b[b_l]:
			f.append(a[a_l])
			a_l += 1
		else:
			f.append(b[b_l])
			b_l += 1

	while (a_l < a_r):
			f.append(a[a_l])
			a_l += 1

	while (b_l < b_r):
			f.append(b[b_l])
			b_l += 1

	result = " ".join(map(str, f))
	print(result)
	return result


#I/O - better to create separate __init__ function

n = int(input()) 
a = [int(x) for x in input().split()]
m = int(input()) 
b = [int(x) for x in input().split()]

a_l = 0
b_l = 0
a_r = len(a)
b_r = len(b)

merge(a_l, a_r, b_l, b_r)
