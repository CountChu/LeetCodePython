from data_structure import *
import pdb

def test(sln, nums, p, q, answer):
    print('nums = %s, p = %d, q = %d, answer = %d' % (nums, p, q, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    out = sln.lowestCommonAncestor(root, sln.module.TreeNode(p), sln.module.TreeNode(q))
    assert out.val == answer, out.val

def run(sln):
    test(sln, [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6)
    test(sln, [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2)
    test(sln, [2, 1], 2, 1, 2)
    test(sln, [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6)
    