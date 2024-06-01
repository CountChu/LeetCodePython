
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target):
    print("nums = %s, target = %s" % (nums, target))
    out = sln.canJump(nums)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [2, 3, 1, 1, 4], True)
    test_solution(sln, [3, 2, 1, 0, 4], False)
    test_solution(sln, [0], True)
    test_solution(sln, [2,0,0], True)
    test_solution(sln, [0,2,3], False)    
    test_solution(sln, [1,0,2,2,0], False)
    test_solution(sln, [3,0,8,2,0,0,1], True)