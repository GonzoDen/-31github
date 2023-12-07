def find_max(arr):
	if not arr:
		return None # return None for an empty list

	minim = arr[0] 
	for i in range(len(arr)):
		if arr[i] < minim:
			minim = arr[i]
	return minim

minim_2 = find_max([1, 2, 3, 0, 6])
print(minim_2)
