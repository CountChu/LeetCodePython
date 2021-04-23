def test(sln, a, b, target):
    out = sln.addBinary(a, b)
    print('a = %s, b = %s, out = %s' % (a, b, out))
    assert out == target
        
def run(sln):        
    test(sln, '11', '1', '100')
    test(sln, '1010', '1011', '10101')
    test(sln, '0', '0', '0')