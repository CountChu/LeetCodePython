import pdb

def test(sln, ls, left, right, answer):
    print('ls = %s, left = %d, right = %d, answer = %s' % (ls, left, right, answer))
    head = sln.ls_to_ll(ls)
    
    out = sln.reverseBetween(head, left, right)
    out_ls = sln.ll_to_ls(out)

    assert out_ls == answer, out_ls

def run(sln):
    test(sln, [1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5])
    test(sln, [5], 1, 1, [5])
