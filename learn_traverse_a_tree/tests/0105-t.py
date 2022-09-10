from data_structure import *
import pdb

def test(sln, preorder, inorder, answer):
    print('preorder = %s, inorder = %s, answer = %s' % (preorder, inorder, answer))
    out = sln.buildTree(preorder, inorder)
    out_ls = binary_tree_v2.tree_to_ls(out)
    assert out_ls == answer, out_ls

def run(sln):
    test(sln, [3,9,20,15,7], [9,3,15,20,7], [3,9,20,None,None,15,7])
    test(sln, [-1], [-1], [-1])


