from data_structure import *
import pdb

def test(sln, inorder, postorder, answer):
    print('inorder = %s, postorder = %s, answer = %s' % (inorder, postorder, answer))
    out = sln.buildTree(inorder, postorder)
    out_ls = binary_tree_v3.tree_to_ls(out)
    assert out_ls == answer, out_ls

def run(sln):
    test(sln, [9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7])
    test(sln, [1, 2, 3, 4], [2, 1, 4, 3], [3, 1, 4, None, 2])
    test(sln, [-1], [-1], [-1])
