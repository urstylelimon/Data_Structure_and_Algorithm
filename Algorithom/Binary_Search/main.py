nums = [3,4,5,6,7,8]
target = 8

low = 0
high = len(nums)-1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        print(f"Target value index number {mid} ")
        break
    else:
        if target < nums[mid]:
            high = mid-1
        else:
            if target > nums[mid]:
                low = mid+1