import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    out = sln.preorderTraversal(nums)
    assert out == answer, out

def run(sln):
    test(sln, [1,null,2,3], [1,2,3])
    #test(sln, [], [])
    #test(sln, [1], [1])
    #test(sln, [1,2], [1,2])
    #test(sln, [1,null,2], [1,2])
