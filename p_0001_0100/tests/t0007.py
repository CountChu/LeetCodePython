def test(s, x, target):
    out = s.reverse(x)
    print('x = %d, out = %d' % (x, out))
    assert out == target

def run(sln):
    test(sln, 4321, 1234)
    test(sln, 123, 321)
    test(sln, -123, -321)
    test(sln, 120, 21)
    test(sln, 1534236469, 0)
