import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %d' % (nums, answer))
    out = sln.maxSubArray(nums)
    assert out == answer, out

def run(sln):
    test(sln, [-1, 0, -2], 0)
    test(sln, [-2, -1], -1)
    test(sln, [-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    test(sln, [1], 1)
    test(sln, [5, 4, -1, 7, 8], 23)
    test(sln, [5, 9, -9, 0, 8], 14)

