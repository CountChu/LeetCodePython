import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    out = sln.findDisappearedNumbers(nums)
    assert out == answer, out

def run(sln):
    test(sln, [4, 3, 2, 7, 8, 2, 3, 1], [5,6])
    test(sln, [1, 1], [2])
