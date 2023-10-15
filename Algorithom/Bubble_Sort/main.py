nums = [6,2,5,1,1,3,4]
n = 1
for i in range(len(nums)):
    j = 0
    while j < len(nums)-n:
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
        j += 1
    n += 1

print(nums)
