from src.select_sort import select_sort

def test_select_sort1():
  nums = [3,5,1]
  assert select_sort(nums) == [1,3,5]

def test_select_sort2():
  nums = [5,3,1]
  assert select_sort(nums) == [1,3,5]

def test_select_sort3():
  nums = [1,5,9,2,0,3]
  assert select_sort(nums) == [0,1,2,3,5,9]

def test_select_sort4():
  nums = [1,5,4,2,0,3]
  assert select_sort(nums) == [0,1,2,3,4,5]
