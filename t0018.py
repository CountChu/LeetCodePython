import pdb

def test(sln, nums, target, answer):
    print('nums = %s, target = %d, answer = %s' % (nums, target, answer))
    out = sln.fourSum(nums, target)
    out.sort()
    answer.sort()
    assert out == answer, out

def run(sln):
    test(sln, [1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
    test(sln, [2,2,2,2,2], 8, [[2,2,2,2]])
