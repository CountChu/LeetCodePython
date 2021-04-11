def test(sln, nums1, nums2, target):
    out = sln.findMedianSortedArrays(nums1, nums2)
    print(nums1, nums2, out)
    assert out == target

def run(sln):
    test(sln, [3], [-2, -1], -1)   
    test(sln, [1, 3], [2], 2)
    test(sln, [1, 2], [3, 4], 2.5)
    test(sln, [0, 0], [0, 0], 0)
    test(sln, [], [1], 1)
    test(sln, [2], [], 2)