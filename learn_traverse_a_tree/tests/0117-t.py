from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    ls = binary_tree_v3.tree_to_ls(root)
    #pdb.set_trace()
    assert nums == ls

    out = sln.connect(root)
    #pdb.set_trace()
    out_ls = sln.tree_to_ls(out)
    assert out_ls == answer, out_ls

def run(sln):
    test(sln, [1,2,3,4,5,None,7], [1,'#',2,3,'#',4,5,7,'#'])
    test(sln, [], [])
    test(sln, [1,2,None,3,None,4,None,5], [1,'#',2,'#',3,'#',4,'#',5,'#'])
    test(
    	sln, 
    	[1, 2, 3, 4, 5, 6, 7, None, None, 8, 9],
    	[1, '#', 2, 3, '#', 4, 5, 6, 7, '#', 8, 9, '#']
    	)
