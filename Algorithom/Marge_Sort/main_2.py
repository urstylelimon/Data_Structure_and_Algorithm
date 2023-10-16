def merge_sort(list):

  result = []

  if len(list) <= 1:
    return list

  mid = len(list) // 2
  left = merge_sort(list[:mid])
  right = merge_sort(list[mid:])


  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  while i < len(left):
    result.append(left[i])
    i += 1
  while j < len(right):
    result.append(right[j])
    j += 1

  return result


unsorted_list = [5, 3, 2, 1, 4]
sorted_array = merge_sort(unsorted_list)

print(sorted_array)
