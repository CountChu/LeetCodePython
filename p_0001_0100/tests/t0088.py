        
def test(sln, nums1, m, nums2, n, target):
    out = nums1.copy()
    sln.merge(out, m, nums2, n)
    #pdb.set_trace()
    print('nums1 = %s, m = %d, num2 = %s, n = %d, out = %s' % (nums1, m, nums2, n, out))
    assert out == target
        
def run(sln):
    test(sln, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
    test(sln, [1], 1, [], 0, [1])   