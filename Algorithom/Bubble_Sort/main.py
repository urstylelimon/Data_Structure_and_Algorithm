nums = [6,2,5,1,1,3,4]

n = len(nums)
flag = 1
while flag < n:
    for i in range(len(nums)):
        for k in range(i+1, len(nums)):
            if nums[i] > nums[k]:
                nums[i],nums[k] = nums[k],nums[i]
                break
    flag += 1

print(nums)
