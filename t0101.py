def test(sln, root_ls, target):
    root = sln.build_tree(root_ls)
    #pdb.set_trace()
    out = sln.isSymmetric(root)
    print('root_ls = %s, out = %s' % (root_ls, out))
    assert out == target
        
def run(sln):        
    test(sln,  [0, 1, 2, 3, 4, 5, 6], False)
    test(sln,  [1, 2, 2, 3, 4, 4, 3], True)
    test(sln,  [1, 2, 2, None, 3, None, 3], False)