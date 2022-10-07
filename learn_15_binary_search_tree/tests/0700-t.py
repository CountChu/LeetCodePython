from data_structure import *
import pdb

def test(sln, nums, val, answer):
    print('nums = %s, val = %d, answer = %s' % (nums, val, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    out = sln.searchBST(root, val)
    out_ls = binary_tree_v3.tree_to_ls(out)
    assert out_ls == answer, out_ls

def run(sln):
    test(sln, [4, 2, 7, 1, 3], 2, [2, 1, 3])
    test(sln, [4, 2, 7, 1, 3], 5, [])
