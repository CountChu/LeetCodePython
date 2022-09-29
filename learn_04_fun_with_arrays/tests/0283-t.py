import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    out = nums.copy()
    sln.moveZeroes(out)
    assert out == answer, out

def run(sln):
    test(sln, [0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
    test(sln, [0], [0])
    test(sln, [0, 0, 1], [1, 0, 0])
