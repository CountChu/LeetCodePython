import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    out = sln.sortedSquares(nums)
    assert out == answer, out

def run(sln):
    test(sln, [-4, -1, 0, 3, 10], [0, 1, 9, 16, 100])
    test(sln, [-7, -3, 2, 3, 11], [4, 9, 9, 49, 121])
