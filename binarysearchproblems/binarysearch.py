def binarysearch(arr,target):
  left = 0
  right = len(arr)-1

  while left < right:
    mid = (left+right) // 2

    if arr[mid] == target:
      return mid 
    elif arr[mid] < target:
      left += 1
    else:
      right -= 1
  return -1
