from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    #pdb.set_trace()
    root = binary_tree_v3.ls_to_tree(nums)
    nums_2 = binary_tree_v3.tree_to_ls(root)
    assert nums == nums_2

    out = sln.levelOrder(root)
    assert out == answer, out

def run(sln):
    test(sln, [3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]])
    test(sln, [1], [[1]])
    test(sln, [], [])
    test(sln, [1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]])