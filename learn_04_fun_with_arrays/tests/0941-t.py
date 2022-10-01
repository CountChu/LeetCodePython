import pdb

def test(sln, arr, answer):
    print('arr = %s, answer = %d' % (arr, answer))
    out = sln.validMountainArray(arr)
    assert out == answer, out

def run(sln):
    test(sln, [2], False)
    test(sln, [2, 1], False)
    test(sln, [3, 5, 5], False)
    test(sln, [0, 3, 2, 1], True)
    test(sln, [6, 7, 7, 8, 6], False)
    test(sln, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], False)
