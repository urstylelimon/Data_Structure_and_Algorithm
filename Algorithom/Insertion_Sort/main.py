nums = [1,3,5,3,33,4,5,5,27,26,25,24,23,3,22,21,20]
for i in range(1, len(nums)):
    val = nums[i] #4
    key = 1
    s = i
    for j in range(i):
        if val < nums[i-key]:
            nums[s], nums[i-key] = nums[i-key], val
            s -= 1
        if val > nums[i-key]:
            break
        key += 1

print(nums)