from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    nums_1 = binary_tree_v3.tree_to_ls(root)
    assert nums == nums_1

    out = sln.postorderTraversal(root)
    assert out == answer, out

def run(sln):
    test(sln, [0,1,2,3,4,5,6,7,8], [7,8,3,4,1,5,6,2,0])
    test(sln, [1,None,2,3], [3,2,1])
    test(sln, [], [])
    test(sln, [1], [1])
    test(sln, [1, 2], [2, 1])
    test(sln, [1,None,2], [2,1])


