def test(sln, x, target):
    print('x = %d, target = %d' % (x, target))
    out = sln.mySqrt(x)
    assert out == target, out
        
def run(sln):
    test(sln, 3, 1)
    test(sln, 2, 1)
    test(sln, 1, 1)     
    test(sln, 4, 2)
    test(sln, 8, 2)
    test(sln, 100, 10)
    test(sln, 0, 0)