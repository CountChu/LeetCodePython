def test(sln, x, target):
    out = sln.mySqrt(x)
    print('x = %d, out = %d' % (x, out))
    assert out == target
        
def run(sln):
    test(sln, 2, 1)
    test(sln, 1, 1)     
    test(sln, 4, 2)
    test(sln, 8, 2)
    test(sln, 100, 10)