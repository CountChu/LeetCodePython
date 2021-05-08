from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    root = binary_tree_v2.ls_to_tree(nums)
    out = sln.connect(root)
    out_ls = sln.tree_to_ls(out)
    assert out_ls == answer, out_ls

def run(sln):
    test(sln, [], [])
    test(sln, [1,2,3,4,5,6,7], [1,'#',2,3,'#',4,5,6,7,'#'])