def test(sln, head, target):
    head_ll = sln.to_ll(head)
    out_ll = sln.deleteDuplicates(head_ll)
    out = sln.to_array(out_ll)
    print('head = %s, out = %s' % (head, out))
    assert out == target
        
def run(sln):        
    test(sln, [], [])      
    test(sln, [1, 1, 2], [1, 2])
    test(sln, [1, 1, 2, 3, 3], [1, 2, 3])  