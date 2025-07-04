nums = [3,4,5,6,7,8,9]
target = 9

low = 0
high = len(nums) - 1

flag = True
while flag:
    mid = (low + high) // 2

    if target == nums[mid]:
        print("Node found at index: ", mid)
        break

    if target < nums[mid]:
        high = mid - 1

    if target > nums[mid]:
        low = mid +1

    if mid == len(nums) - 1:
        print("Not Found")
        break