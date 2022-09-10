from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    nums_1 = binary_tree.transform_ls(nums)
    root = binary_tree.ls_to_tree(nums_1)
    nums_2 = binary_tree.tree_to_ls(root)
    assert nums_1 == nums_2

    out = sln.postorderTraversal(root)
    assert out == answer, out

def run(sln):
    test(sln, [0,1,2,3,4,5,6,7,8], [7,8,3,4,1,5,6,2,0])
    test(sln, [1,None,2,3], [3,2,1])
    test(sln, [], [])
    test(sln, [1], [1])
    test(sln, [1, 2], [2, 1])
    test(sln, [1,None,2], [2,1])


