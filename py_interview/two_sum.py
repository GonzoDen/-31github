"""

def two_sum(nums, target):
	arr = []
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] + nums[j] == target:
				arr.append(i)
				arr.append(j)
	return arr"""

def two_sum(nums, target):
    num_indices = {}  # Dictionary to store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            return [num_indices[complement], i]

        num_indices[num] = i

    return []  # Return an empty list if no pair is found

nums = [2, 3, 7, 12]
target = 9
print(two_sum(nums, target))