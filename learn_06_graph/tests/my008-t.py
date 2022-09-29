
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, x, target):
    print("nums = %s, x = %d, target = %s" % (nums, x, target))
    out = sln.find_root(nums, x)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [0, 0, 1, 2, 3, 4], 5, 0)
    test_solution(sln, [0, 0, 1, 2, 3, 4], 2, 0)
    test_solution(sln, [1, 8, 1, 8, 3, 0, 5, 1, 8, 8], 9, 8)
                      # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    test_solution(sln, [1, 8, 1, 8, 3, 0, 5, 1, 8, 8], 7, 8)
    test_solution(sln, [1, 8, 1, 8, 3, 0, 5, 1, 8, 8], 6, 8)
