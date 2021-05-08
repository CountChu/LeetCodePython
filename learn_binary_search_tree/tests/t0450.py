from data_structure import *
import pdb

def test(sln, nums, key, answer):
    print('nums = %s, key = %d, answer = %s' % (nums, key, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    root = sln.deleteNode(root, key)
    root_ls = binary_tree_v3.tree_to_ls(root)
    assert root_ls == answer, root_ls

def run(sln, module):
    if True:
        test(sln, [5,3,6,2,4,None,7], 3, [5,4,6,2,None,None,7])
        test(sln, [5,3,6,2,4,None,7], 5, [6,3,7,2,4])
        test(sln, [5,3,6,2,4,None,7], 0, [5,3,6,2,4,None,7])
        test(sln, [], 0, [])
        test(sln, [0], 0, [])
        test(sln, [50,30,70,None,40,60,80], 50, [60,30,70,None,40,None,80])
        test(sln, [3,2,5,None,None,4,10,None,None,8,15,7], 5, [3,2,7,None,None,4,10,None,None,8,15])
        test(sln, [1,None,2], 1, [2])

    if True:
        test(
            sln,
            [
                2,
                0, 33,
                None, 1, 25, 40,
                None, None, None, None, 34, 45,
                None, 36, None, None,
                35, 39
            ],
            33,
            [
                2,
                0, 34,
                None, 1, 25, 40,
                None, None, None, None, 36, 45,
                35, 39
            ],
            )

