def test(sln, nums, val, answer_nums, answer_len):
    print('nums = %s, val = %d, answer_nums = %s, answer_len = %d' % (nums, val, answer_nums, answer_len))	
    new_nums = nums.copy()
    new_val = sln.removeElement(new_nums, val)
    assert new_val == answer_len, new_val
    assert new_nums[:new_val] == answer_nums, new_nums[:new_val]
        
def run(sln):
    test(sln, [3, 2, 2, 3], 2, [3, 3], 2)
    test(sln, [3, 2, 2, 3], 3, [2, 2], 2)
    test(sln, [0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4], 5)