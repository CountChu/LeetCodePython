from data_structure import *
import pdb
br = pdb.set_trace

def test(sln, n, answer):
    print('n = %d, answer = %s' % (n, answer))
    out = sln.generateTrees(n)
    out_ls_ls = []
    for nd in out:
        out_ls_ls.append(binary_tree_v3.tree_to_ls(nd))
    assert out_ls_ls == answer, out_ls_ls

def run(sln):
    if False:
        test(
            sln,
            1,
            [[1]],
        )

    if False:
        test(
            sln,
            2,
            [
                [1, None, 2],
                [2, 1]
            ],
        )        

    if True:
        test(
            sln, 
            3, 
            [
                [1, None, 2, None, 3],
                [1, None, 3, 2],
                [2, 1, 3],
                [3, 1, None, None, 2],
                [3, 2, None, 1]
            ]
        )

