
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, t, target):
    print("nums = %s, t = %d, target = %d" % (nums, t, target))
    out = sln.search(nums, t)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [-1, 0, 3, 5, 9, 12], 9, 4)
    test_solution(sln, [-1, 0, 3, 5, 9, 12], 2, -1)
    test_solution(sln, [-1, 0, 3, 5, 9, 12], 0, 1)    
    test_solution(sln, [5], -5, -1)
    test_solution(sln, [5], 5, 0)
    test_solution(sln, [1, 5], 5, 1)
    test_solution(sln, [2, 5], 2, 0)
    test_solution(sln, [-1,0,3,5,9,12], 13, -1)
    test_solution(sln, [-1,0,5], 5, 2)