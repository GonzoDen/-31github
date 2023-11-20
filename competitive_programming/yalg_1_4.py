def merge_sort (arr):
	f = [] * len(arr)

	def recursive_sort (a_s, a_e):
		if a_e <= a_s: return

		mid = (a_s + a_e) // 2
		recursive_sort(a_s, mid)
		recursive_sort(mid+1, a_e)
		merge(a_s, mid, a_e)

	def merge(a_s, mid, a_e):

	#lo = a_l = left
	#mid = a_r 
	#mid+1=b_l
	#hi = b_r

		a_l = a_s
		a_r = mid
		b_l = mid+1
		b_r = a_e

		while (b_l <= b_r) and (a_l < a_r):
			if arr[a_l] > arr[b_l]:
				f.append(arr[b_l])
				b_l += 1
			else:
				f.append(arr[a_l])
				a_l += 1

		while (a_l < a_r):
				f.append(arr[a_l])
				a_l += 1

		while (b_l < b_r):
				f.append(arr[b_l])
				b_l += 1
	
	recursive_sort(0, len(arr)-1)
	print(f)

n = int(input()) 
arr = [int(x) for x in input().split()]
merge_sort(arr)
#result = " ".join(map(str, arr))
#print(result)


