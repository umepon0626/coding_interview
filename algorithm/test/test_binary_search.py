from src.binary_search import binary_search
import pytest

@pytest.mark.timeout(1)
def test_binary_search1():
  test_arr = [1,2,3,4,5,6,7,8]
  assert binary_search(test_arr, target=4) == 3

@pytest.mark.timeout(1)
def test_binary_search2():
  test_arr = [1,3,4,6,8,14,30]
  assert binary_search(test_arr, target=5) == -1

@pytest.mark.timeout(1)
def test_binary_search3():
  test_arr = [1,3,4,6,8,14,30]
  assert binary_search(test_arr, target=30) == 6