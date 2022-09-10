import pdb

def test(sln, heights, answer):
    print('heights = %s, answer = %d' % (heights, answer))
    out = sln.heightChecker(heights)
    assert out == answer, out

def run(sln):
    test(sln, [1,1,4,2,1,3], 3)
    test(sln, [5,1,2,3,4], 5)
    test(sln, [1,2,3,4,5], 0)


