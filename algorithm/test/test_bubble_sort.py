from src import bubble_sort

def test_bubble_sort1():
  test_arr = [1,4,6,2,5]
  assert bubble_sort.bubble_sort(test_arr) == [1,2,4,5,6]

def test_bubble_sort2():
  test_arr = [1,3,4,6,2,5]
  assert bubble_sort.bubble_sort(test_arr) == [1,2,3,4,5,6]

def test_bubble_sort3():
  test_arr = [2,1]
  assert bubble_sort.bubble_sort(test_arr) == [1,2]