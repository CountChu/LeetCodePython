def test(sln, nums, target, answer):
    print('nums = %s, target = %d, answer = %d' % (nums, target, answer))
    out = sln.searchInsert(nums, target)
    assert out == answer, out
        
def run(sln):
    test(sln, [1, 3, 5, 6], 5, 2)
    test(sln, [1, 3, 5, 6], 2, 1)
    test(sln, [1, 3, 5, 6], 7, 4)
    test(sln, [1, 3, 5, 6], 0, 0)
    test(sln, [1], 0, 0)