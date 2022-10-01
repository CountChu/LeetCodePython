def test(sln, nums, answer_nums, answer_count):
    print('nums = %s, answer_nums = %s, answer_count = %d' % (nums, answer_nums, answer_count))	
    new_nums = nums.copy()
    count = sln.removeDuplicates(new_nums)
    assert count == answer_count, count
    assert new_nums[:count] == answer_nums
        
def run(sln):

    test(sln, [1, 1, 2], [1, 2], 2)
    test(sln, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5)