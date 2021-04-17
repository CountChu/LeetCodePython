def test(sln, nums, target, target_out):
    print('nums = %s, target = %d, target_out = %s' % (nums, target, target_out))
    out = sln.twoSum(nums, target)
    assert out == target_out, out
    print('')

def run(sln):

    test(sln, [1,6142,8192,10239], 18431, [3, 2])
    #test(sln, [3, 2, 3], 6, [0, 2])
    #test(sln, [1, 2, 7, 11, 15], 9, [1, 2])
    #test(sln, [2, 7, 11, 15], 9, [0, 1])
    #test(sln, [2, 3, 4], 6, [0, 2])
    #test(sln, [3, 3], 6, [0, 1])
    #test(sln, [2, 5, 5, 11], 10, [1, 2])
    #test(sln, [15, 11, 7, 2, 1], 9, [3, 2])
    #test(sln, [3, 2, 4], 6, [1, 2])
    