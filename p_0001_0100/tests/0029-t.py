import pdb

def test(sln, dividend, divisor, answer):
    print('dividend = %s, divisor = %d, answer = %d' % (dividend, divisor, answer))
    out = sln.divide(dividend, divisor)
    assert out == answer, out

def run(sln):
    test(sln, 110, 3, 36)
    test(sln, 10, 3, 3)
    test(sln, 7, -3, -2)
    test(sln, 0, 1, 0)
    test(sln, 1, 1, 1)
    test(sln, -1, 1, -1)
    test(sln, -2147483648, -1, 2147483647)


