def test(sln, ls1, ls2, target):
    
    l1 = sln.to_linked_list(ls1)
    #pdb.set_trace()
    l2 = sln.to_linked_list(ls2)
    out = sln.addTwoNumbers(l1, l2)
    out_ls = sln.to_list(out)
    print('ls1 = %s, ls2 = %s, out_ls = %s' % (ls1, ls2, out_ls))
    assert out_ls == target
    print('')

def run(sln):

    test(sln, [2,4,3], [5,6,4], [7,0,8])
    test(sln, [0], [0], [0])
    test(sln, [9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])

