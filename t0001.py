def test(sln, nums, target, target_out):
    out = sln.twoSum(nums, target)
    print('nums = %s, target = %d, out = %s' % (nums, target, out))
    assert out == target_out
    print('')

def run(sln):

    test(sln, [2, 7, 11, 15], 9, [0, 1])
    test(sln, [3, 2, 4], 6, [1, 2])
    test(sln, [3, 3], 6, [0, 1])
    test(sln, [2, 5, 5, 11], 10, [1, 2])