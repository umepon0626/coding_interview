# the methods shown below are documented in https://www.google.com/search?q=%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0+%E8%8B%B1%E8%AA%9E&oq=%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0%E3%80%80%E8%8B%B1%E8%AA%9E&aqs=edge..69i57j0i30j0i8i30l2.3902j0j4&sourceid=chrome&ie=UTF-8
from typing import List
class Heap:
  def __init__(self):
    self.arr = []
  
  def __modify_partial(self, index):
    if index <= 0:
      return
    parent_index = index // 2
    if self.arr[parent_index] > self.arr[index]:
      self.arr[parent_index], self.arr[index] = self.arr[index], self.arr[parent_index]
      self.__modify_partial(parent_index)
    return
  
  def heappush(self, item: int) -> None:
    self.arr.append(item)
    self.__modify_partial(len(self.arr)-1)


  def heappop(self) -> int:
    """
    return the minimum value
    """
    
    dst = self.arr[0]
    if len(self.arr) == 1:
      return self.arr.pop(-1)
    self.arr[0] = self.arr.pop(-1) #O(1)
    max_index = len(self.arr) - 1
    index = 1
    
    if index == max_index and self.arr[index-1] > self.arr[index]:
      self.arr[index], self.arr[index - 1] = self.arr[index-1], self.arr[index]

    while index < max_index:
      if self.arr[index] < self.arr[index+1]:
        self.arr[(index-1) // 2 ], self.arr[index] = self.arr[index], self.arr[(index-1) // 2 ]
        index = index * 2 + 1
      else:
        self.arr[(index-1) // 2 ], self.arr[index+1] = self.arr[index+1], self.arr[(index-1) // 2 ]
        index = (index + 1) * 2
    return dst

  def heappushpop(self, item: int) -> int:
    self.heappush(item)
    return self.pop()
  
  def heapify(self, nums: List[int]) -> None:
    """
    create heap from List[int]
    """
    for n in nums:
      self.heappush(n)
    
  
  def heapreplace(self, item: int) -> int:
    dst = self.heappop()
    self.heappush(item)
    return dst
