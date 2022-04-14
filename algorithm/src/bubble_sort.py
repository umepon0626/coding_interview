from typing import List
def bubble_sort(nums: List[int]) -> List[int]:
  for i in range(1,len(nums)):
    for k in range(1,len(nums)+1-i):
      if nums[k]<nums[k-1]:
        nums[k], nums[k-1] = nums[k-1], nums[k]
      print(nums)
  return nums

