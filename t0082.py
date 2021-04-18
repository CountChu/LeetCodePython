import pdb

def test(sln, ls, answer):
    print('ls = %s, answer = %s' % (ls, answer))
    
    head = sln.ls_to_ll(ls)
    out = sln.deleteDuplicates(head)
    out_ls = sln.ll_to_ls(out)

    assert out_ls == answer, out_ls

def run(sln):
    test(sln, [1, 2, 3, 3, 4, 4, 5], [1, 2, 5])
    test(sln, [1, 1, 1, 2, 3], [2, 3])
