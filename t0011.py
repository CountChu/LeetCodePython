def test(sln, height, target):
    print('height = %s' % height)
    out = sln.maxArea(height)
    print('out = %d' % out)
    assert out == target        

def run(sln):

    test(sln, [1,8,6,2,5,4,8,3,7], 49)
    test(sln, [1,1], 1)
    test(sln, [4,3,2,1,4], 16)
    test(sln, [1,2,1], 2)