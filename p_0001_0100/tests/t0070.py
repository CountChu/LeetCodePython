def test(sln, n, target):
    out = sln.climbStairs(n)
    print('n = %d, out = %d' % (n, out))
    assert out == target

def run(sln):

    test(sln, 1, 1)                         # 1
    test(sln, 2, 2)                         # 1 + 1, 2
    test(sln, 3, 3)                         # 1 + 1 + 1, 1 + 2, 2 + 1

    test(sln, 4, 5)                         # 1 + 1 + 1 + 1
                                            # 1 + 1 + 2
                                            # 2 + 2
       
    test(sln, 35, 14930352)      