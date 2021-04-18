import pdb

def test(sln, ls, k, answer):
    print('ls = %s, k = %d, answer = %s' % (ls, k, answer))
    head = sln.list_to_ll(ls)
    out = sln.rotateRight(head, k)
    
    out_ls = sln.ll_to_list(out)
    assert out_ls == answer, out_ls

def run(sln):
    #test(sln, [1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3])
    #test(sln, [0, 1, 2], 4, [2, 0, 1])
	#test(sln, [], 0, [])
	test(sln, [1, 2, 3], 2000000000, [2, 3, 1])