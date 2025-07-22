nums = [5,2,4,1]

for i in range(1,len(nums)):
    j = nums[i-1]
    i = nums[i]

    while nums.index(j) >= 0 :

        if nums.index(j) == 0:

            if j > i:
               nums[nums.index(j)], nums[nums.index(i)] = i, j


        elif j > i:
            nums[nums.index(j)], nums[nums.index(i)] = i, j
        j -= 1

    print(nums)