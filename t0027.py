def test(sln, nums, val, target_nums, target_val):
    new_nums = nums.copy()
    new_val = sln.removeElement(new_nums, val)
    print('nums = %s, val = %d, new_nums = %s, new_val = %d' % (nums, val, new_nums, new_val))
    assert new_val == target_val
    assert new_nums[:new_val] == target_nums
        
def run(sln):
    test(sln, [3,2,2,3], 3, [2,2], 2)
    test(sln, [0,1,2,2,3,0,4,2], 2, [0,1,3,0,4], 5)