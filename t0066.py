def test(sln, digits, target):
    out = sln.plusOne(digits)
    print('digits = %s, out = %s' % (digits, out))
    assert out == target
    
def run(sln):    
    test(sln, [1, 2, 3], [1, 2, 4])
    test(sln, [4, 3, 2, 1], [4, 3, 2, 2])
    test(sln, [0], [1])
    test(sln, [1, 2, 9], [1, 3, 0])
    test(sln, [9], [1, 0])