# the methods shown below are documented in https://www.google.com/search?q=%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0+%E8%8B%B1%E8%AA%9E&oq=%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0%E3%80%80%E8%8B%B1%E8%AA%9E&aqs=edge..69i57j0i30j0i8i30l2.3902j0j4&sourceid=chrome&ie=UTF-8
from typing import List
class Heap:
  def heappush(self, item: int) -> None:
    pass
  def heappop(self) -> int:
    """
    return the minimum value
    """
    pass
  def heappushpop(self, item: int) -> int:
    self.heappush(item)
    return self.pop()
  
  def heapify(self, nums: List[int]) -> None:
    """
    create heap from List[int]
    """
    pass
  
  def heapreplace(self, item: int) -> int:
    dst = self.heappop()
    self.heappush(item)
    return dst

  
