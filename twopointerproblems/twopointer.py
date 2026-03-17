def twopointer(arr,target):
  left = 0
  right = len(arr)-1
  while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum == target:
      return left,right
    elif current_sum < target:
      right -= 1
    else:
      left += 1
  return None


