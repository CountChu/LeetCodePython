def test(sln, n, answer):
    print('n = %d, answer = %d' % (n, answer))
    out = sln.climbStairs(n)
    assert out == answer, out

def run(sln):

    test(sln, 1, 1)                        
    test(sln, 2, 2)                        
    test(sln, 3, 3)                        
    test(sln, 4, 5)
    test(sln, 35, 14930352)      