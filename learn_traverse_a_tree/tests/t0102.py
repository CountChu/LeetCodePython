from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    ls1 = binary_tree.transform_ls(nums)
    #pdb.set_trace()
    root = binary_tree.ls_to_tree(ls1)
    ls2 = binary_tree.tree_to_ls(root)
    assert ls1 == ls2
    #pdb.set_trace()

    out = sln.levelOrder(root)
    assert out == answer, out

def run(sln):
    test(sln, [3,9,20,None,None,15,7], [[3],[9,20],[15,7]])
    test(sln, [1], [[1]])
    test(sln, [], [])
    test(sln, [1,2,3,4,None,None,5], [[1],[2,3],[4,5]])