import pdb
br = pdb.set_trace

from data_structure import *

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    nums1 = binary_tree_v3.tree_to_ls(root)
    assert nums == nums1
    
    out = sln.inorderTraversal(root)
    assert out == answer, out

def test_(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    nums_1 = binary_tree.transform_ls(nums)
    root = binary_tree.ls_to_tree(nums_1)
    nums_2 = binary_tree.tree_to_ls(root)
    assert nums_1 == nums_2, nums_1

    out = sln.inorderTraversal(root)
    assert out == answer, out

def run(sln):
    test(sln, [0, 1, 2, 3, 4, 5, 6, 7, 8], [7, 3, 8, 1, 4, 0, 5, 2, 6])
    test(sln, [1, None, 2, 3], [1, 3, 2])
    test(sln, [], [])
    test(sln, [1], [1])
    test(sln, [1, 2], [2, 1])
    test(sln, [1, None, 2], [1, 2])
