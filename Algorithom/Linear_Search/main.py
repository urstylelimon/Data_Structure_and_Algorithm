nums = [65,54,76,23,65,33,77,53,23,98,24]
target = 98
result = []
for i in range(len(nums)):
    if nums[i] == target :
        result.append(i)
        break

if result != []:
    print("The Index of target value :", i)
else:
    print("The Traget value is not availabe in nums")

