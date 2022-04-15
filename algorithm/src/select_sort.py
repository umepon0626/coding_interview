from typing import List
def select_sort(nums: List[int]) -> List[int]:
  # nums = [3,5,1,2,6]
  for i in range(len(nums)):
    # i = 3
    min_index = i # 3
    min_value = nums[i] # 5
    for k in range(i+1, len(nums)):
      # k=4
      if nums[k] < min_value: # 6 < 3 pass
        min_index = k # 3
        min_value = nums[k] # 2
    if i != min_index: # 2 != 2
      nums[i], nums[min_index] = nums[min_index], nums[i]
    # nums = [1,2,3,5,6]
  return nums




