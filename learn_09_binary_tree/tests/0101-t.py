from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %d' % (nums, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    nums2 = binary_tree_v3.tree_to_ls(root)
    assert nums == nums2

    out = sln.isSymmetric(root)
    assert out == answer, out
        
def run(sln): 
    test(sln, [1], True)
    test(sln, [1,2,2,2,None,2], False)       
    test(sln, [1, None, 2, 3], False)
    test(sln, [0, 1, 2, 3, 4, 5, 6], False)
    test(sln, [1, 2, 2, 3, 4, 4, 3], True)
    test(sln, [1, 2, 2, None, 3, None, 3], False)
    test(sln, [0, 1, 1, 3, 4, 4, 3, 1, 2, 3, 4, 4, 3, 2, 1], True)