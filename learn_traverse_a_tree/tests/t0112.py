from data_structure import *
import pdb

def test(sln, nums, targetSum, answer):
    print('nums = %s, targetSum = %d, answer = %s' % (nums, targetSum, answer))
    ls1 = binary_tree_v2.transform_ls(nums)
    root = binary_tree_v2.ls_to_tree(ls1)
    ls2 = binary_tree_v2.tree_to_ls(root)
    assert ls1 == ls2

    out = sln.hasPathSum(root, targetSum)
    assert out == answer, out

def run(sln):
    #test(sln, [5,4,8,11,None,13,4,7,2,None,None,None,1], 22, True)
    #test(sln, [1,2,3], 5, False)
    #test(sln, [1,2], 0, False)
    test(sln, [], 1, False)
