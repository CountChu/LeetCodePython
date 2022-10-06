from data_structure import *
import pdb

def test(sln, nums, p, q, answer):
    print('nums = %s, p = %d, q = %d, answer = %d' % (nums, p, q, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    p_n = binary_tree_v3.TreeNode(p)
    q_n = binary_tree_v3.TreeNode(q)
    out = sln.lowestCommonAncestor(root, p_n, q_n)
    assert out.val == answer, out

def run(sln):
    if True:
        test(
            sln, 
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 
            5, 
            1, 
            3)

    if True:
        test(
            sln, 
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 
            5, 
            4, 
            5)
