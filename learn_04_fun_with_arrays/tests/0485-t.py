import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %d' % (nums, answer))
    out = sln.findMaxConsecutiveOnes(nums)
    assert out == answer, out

def run(sln):
    test(sln, [1,1,0,1,1,1], 3)
    test(sln, [1,0,1,1,0,1], 2)

