from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    ls = binary_tree_v3.tree_to_ls(root)
    assert nums == ls, nums
    #pdb.set_trace()

    #nums = sln.tree_to_ls(root)
    #pdb.set_trace()

    out = sln.preorderTraversal(root)

    assert out == answer, out


def run(sln):
    #test(sln, [5,4,8,11,None,13,4,7,2,None,None,None,1], [5,4,11,7,2,8,13,4,1])
    test(sln, [1,2,None,3,None,4,None,5], [1,2,3,4,5])
    test(sln, [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 3, 7, 8, 4, 2, 5, 6])
    test(sln, [1,None,2,3], [1,2,3])
    test(sln, [], [])
    test(sln, [1], [1])
    test(sln, [1,2], [1,2])
    test(sln, [1,None,2], [1,2])
