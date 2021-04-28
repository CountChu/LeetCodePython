        
def test(sln, nums1, m, nums2, n, answer):
    print('nums1 = %s, m = %d, num2 = %s, n = %d, answer = %s' % (nums1, m, nums2, n, answer))

    out = nums1.copy()
    sln.merge(out, m, nums2, n)
    #pdb.set_trace()
    assert out == answer
        
def run(sln):
    test(sln, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
    test(sln, [1], 1, [], 0, [1])   
    test(sln, [0], 0, [1], 1, [1])    