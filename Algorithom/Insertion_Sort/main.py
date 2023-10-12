nums = [6,2,5,1,3,4]

for i in range(1,len(nums)):
    j = i
    while i > 0:
        if nums[i-1] > nums[j]:
            temp = nums[i-1]
            nums[i-1] = nums[j]
            nums[j] = temp
            j = i-1
        else:
            break
        i -= 1

print(nums)


