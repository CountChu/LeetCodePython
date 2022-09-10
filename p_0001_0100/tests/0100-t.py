def test(sln, list1, list2, target):
    p = sln.build_tree(list1)
    q = sln.build_tree(list2)
    #pdb.set_trace()
    out = sln.isSameTree(p, q)
    print('list1 = %s, list2 = %s, out = %s' % (list1, list2, out))
    assert out == target

def run(sln):        
    test(sln, [], [], True)
    test(sln, [1, 2, 3], [1, 2, 3], True)
    test(sln, [1, 2], [1, None, 2], False)
    test(sln, [1, 2, 1], [1, 1, 2], False)
    test(sln, [1, None, 2], [1], False)
    test(sln, [1], [1, None, 2], False)