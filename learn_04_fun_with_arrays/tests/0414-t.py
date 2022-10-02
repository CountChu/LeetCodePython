import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %d' % (nums, answer))
    out = sln.thirdMax(nums)
    assert out == answer, out

def run(sln):
    test(sln, [3, 2, 1], 1)
    test(sln, [1, 2], 2)
    test(sln, [2, 2, 3, 1], 1)
    test(sln, [1, 2, 2, 5, 3, 5], 2)
    test(sln, [5, 2, 4, 1, 3, 6, 0], 4)
