from src.heap import Heap

def test_heap_sort1():
  test_arr = [1,2,3,4,5]
  heap = Heap()
  heap.heapify(test_arr)
  dst = []
  while len(heap.arr):
    dst.append(heap.heappop())
  assert dst == [1,2,3,4,5]


def test_heap_sort2():
  test_arr = [5,4,3,2,1]
  heap = Heap()
  heap.heapify(test_arr)
  dst = []
  while len(heap.arr):
    dst.append(heap.heappop())
  assert dst == [1,2,3,4,5]