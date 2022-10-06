from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %d' % (nums, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    nums2 = binary_tree_v3.tree_to_ls(root)
    assert nums == nums2
    #pdb.set_trace()

    out = sln.maxDepth(root)
    assert out == answer, out

def run(sln):
    test(sln, [1, None, 2, 3], 3)
    test(sln, [3, 9, 20, None, None, 15, 7], 3)
    test(sln, [1, None, 2], 2)
    test(sln, [], 0)
    test(sln, [0], 1)
