import pdb

def test(sln, ls, answer):
    print('ls = %s, answer = %s' % (ls, answer))
    head = sln.list_to_ll(ls)
    #pdb.set_trace()

    out = sln.swapPairs(head)
    
    out_ls = sln.ll_to_list(out)
    assert out_ls == answer, out_ls

def run(sln):
    #test(sln, [1, 2, 3, 4], [2, 1, 4, 3])
    #test(sln, [], [])
    #test(sln, [1], [1])
    test(sln, [1, 2, 3], [2, 1, 3])