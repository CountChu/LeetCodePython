def test(sln, x, target):
    out = sln.isPalindrome(x)
    print('x = %s, out = %s' % (x, out))
    assert out == target        

def run(sln):
    test(sln, 123454321, True)
    test(sln, 121, True)
    test(sln, -121, False)
    test(sln, 10, False)
    test(sln, -101, False)

