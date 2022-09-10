from data_structure import *
import pdb

def test(sln, n, answer):
    print('n = %d, answer = %d' % (n, answer))
    out = sln.generateTrees(nums)
    out_ls_ls = []
    for root in out:
    	out_ls_ls.append(binary_tree_v3.list_to_tree(root))
    assert out_ls_ls == out_ls_ls, out_ls_ls

def run(sln, module):
    test(
    	sln, 
    	3, 
    	[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
    	)

    test(
    	sln,
    	1,
    	[[1]],
    	)