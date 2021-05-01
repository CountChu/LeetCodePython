from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %d' % (nums, answer))
    ls1 = binary_tree_v2.transform_ls(nums)
    root = binary_tree_v2.ls_to_tree(ls1)
    ls2 = binary_tree_v2.tree_to_ls(root)
    assert ls1 == ls2

    out = sln.isSymmetric(root)
    assert out == answer, out
        
def run(sln): 
    test(sln, [1,2,2,2,None,2], False)       
    test(sln,  [1, None, 2, 3], False)
    test(sln,  [0, 1, 2, 3, 4, 5, 6], False)
    test(sln,  [1, 2, 2, 3, 4, 4, 3], True)
    test(sln,  [1, 2, 2, None, 3, None, 3], False)