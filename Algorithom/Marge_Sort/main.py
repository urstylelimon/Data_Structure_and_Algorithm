def marge_list(nums):
    if len(nums) > 1:

        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        marge_list(left)
        marge_list(right)

        i=0
        j=0
        k=0

        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
                k += 1
            else:
                nums[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            nums[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            nums[k] = right[j]
            j = j + 1
            k = k + 1
    return nums

list = [2,6,5,1,7,4,3]

marge_list(list)
print(list)