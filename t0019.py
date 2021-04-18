import pdb

def test(sln, ls, n, answer):
    print('ls = %s, n = %d, answer = %s' % (ls, n, answer))
    head = sln.list_to_ll(ls)
    out = sln.removeNthFromEnd(head, n)
    out_ls = sln.ll_to_list(out)
    assert out_ls == answer, out_ls

def run(sln):
    test(sln, [1, 2, 3, 4, 5], 2, [1, 2, 3, 5])
    test(sln, [1], 1, [])
    test(sln, [1, 2], 1, [1])
    test(sln, [1, 2], 2, [2])

