from data_structure import *
import pdb
br = pdb.set_trace

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    root1 = binary_tree_v3.ls_to_tree(nums)

    codec = sln.module.Codec()
    data = codec.serialize(root1)
    root2 = codec.deserialize(data)
    
    ls2 = binary_tree_v3.tree_to_ls(root2)

    assert ls2 == answer, ls2

def run(sln):
    test(sln, [1,2,3,None,None,4,5], [1,2,3,None,None,4,5])
    test(sln, [1,2,3,None,None,4,5,6,7], [1,2,3,None,None,4,5,6,7])
    test(sln, [], [])
    test(sln, [1], [1])
    test(sln, [1,2], [1,2])

