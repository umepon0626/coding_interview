from typing import List
def binary_search(nums: List[int], target: int) -> int:
  """
  find the index of num from sorted int arr.
  if arr doesn't contain target num, return -1
  """
  #   test_arr = [1,3,4,6,8,14,30]
  # assert binary_search(test_arr, target=30) == 6
  # len nums -> 7
  if not len(nums): # pass
    return -1
  start_range = 0
  end_range = len(nums)-1# 6
  if not end_range and target != nums[0]:
    return -1
  if not end_range and target == nums[0]:
    return 0
  # start range =5 end range = 6
  while start_range < end_range:
    if start_range + 1 == end_range:
      if target == nums[start_range]:
        return start_range
      if target == nums[end_range]:
        return end_range
      break
    med = (start_range + end_range) // 2 # 5
    # target: 30, med: 5 , nums[med] = 14
    if target > nums[med]:
      start_range = med
      continue
    if target < nums[med]: 
      end_range = med
      continue
    if target == nums[med]:
      return med
  return -1



  
  

  



