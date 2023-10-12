nums = [4, 2, 1, 5, 3]

for i in range(len(nums)):
    min_idx = i

    for j in range(i + 1, len(nums)):
        if nums[j] < nums[min_idx]:
            min_idx = j
    temp = nums[i]
    nums[i] = nums[min_idx]
    nums[min_idx] = temp

print(nums)