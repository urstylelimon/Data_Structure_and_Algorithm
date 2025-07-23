nums = [4,2,5,1]

for i in range(1,len(nums)):
    j = i

    while i > 0:
        if nums[i-1] > nums[j]:
            nums[i-1], nums[j] = nums[j], nums[i-1]
            j  -= 1
        i -= 1
print(nums)