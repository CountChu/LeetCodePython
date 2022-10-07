from data_structure import *
import pdb

def test(sln, nums, val, answer):
    print('nums = %s, val = %d, answer = %s' % (nums, val, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    out = sln.insertIntoBST(root, val)
    out_ls = binary_tree_v3.tree_to_ls(out)
    assert out_ls == answer, out_ls

def run(sln):
    test(sln, [], 5, [5])
    test(sln, [4, 2, 7, 1, 3], 5, [4, 2, 7, 1, 3, 5])
    test(sln, [40, 20, 60, 10, 30, 50, 70], 25, [40, 20, 60, 10, 30, 50, 70, None, None, 25])
    test(sln, [4, 2, 7, 1, 3, None, None, None, None, None, None], 5, [4, 2, 7, 1, 3, 5])
