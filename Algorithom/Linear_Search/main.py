nums = [65,54,76,23,65,33,77,53,23,98,24]
target = 98

for i in nums:
    if i == target:
        print("Node found at index: ", nums.index(target))
        break