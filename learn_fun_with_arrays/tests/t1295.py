import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %d' % (nums, answer))
    out = sln.findNumbers(nums)
    assert out == answer, out

def run(sln):
    test(sln, [12,345,2,6,7896], 2)
    test(sln, [555,901,482,1771], 1)
