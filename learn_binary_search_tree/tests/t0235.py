from data_structure import *
import pdb

def test(sln, module, nums, p, q, answer):
    print('nums = %s, p = %d, q = %d, answer = %d' % (nums, p, q, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    out = sln.lowestCommonAncestor(root, module.TreeNode(p), module.TreeNode(q))
    assert out.val == answer, out.val

def run(sln, module):
    test(sln, module, [6,2,8,0,4,7,9,None,None,3,5], 2, 8, 6)
    test(sln, module, [6,2,8,0,4,7,9,None,None,3,5], 2, 4, 2)
    test(sln, module, [2,1], 2, 1, 2)
    test(sln, module, [6,2,8,0,4,7,9,None,None,3,5], 2, 8, 6)
    