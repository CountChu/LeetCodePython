from data_structure import *
import pdb

def test(sln, nums, targetSum, answer):
    print('nums = %s, targetSum = %d, answer = %s' % (nums, targetSum, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    nums2 = binary_tree_v3.tree_to_ls(root)
    assert nums == nums2

    out = sln.hasPathSum(root, targetSum)
    assert out == answer, out

def run(sln):
    test(sln, [1, 2], 1, False)
    test(sln, [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True)
    test(sln, [1, 2, 3], 5, False)
    test(sln, [1, 2], 0, False)
    test(sln, [], 1, False)
