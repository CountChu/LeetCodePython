import pdb

def test(sln, ls, x, answer):
    print('ls = %s, x = %d, answer = %s' % (ls, x, answer))
    head = sln.ls_to_ll(ls)

    out = sln.partition(head, x)
    out_ls = sln.ll_to_ls(out)

    assert out_ls == answer, out

def run(sln):
    test(sln, [1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5])
    test(sln, [2, 1], 2, [1, 2])
