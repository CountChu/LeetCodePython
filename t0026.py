def test(sln, nums, target_nums, target_count):
    new_nums = nums.copy()
    count = sln.removeDuplicates(new_nums)
    print('nums = %s, new_nums = %s, count = %d' % (nums, new_nums, count))
    assert count == target_count
    assert new_nums[:count] == target_nums
        
def run(sln):
    test(sln, [1, 1, 2], [1, 2], 2)
    test(sln, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5)