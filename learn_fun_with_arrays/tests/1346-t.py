import pdb

def test(sln, arr, answer):
    print('arr = %s, answer = %d' % (arr, answer))
    out = sln.checkIfExist(arr)
    assert out == answer, out

def run(sln):
    test(sln, [10, 2, 5, 3], True)
    test(sln, [7, 1, 14, 11], True)
    test(sln, [3, 1, 7, 11], False)
    test(sln, [-2, 0, 10, -19, 4, 6, -8], False)
    test(sln, [-20, 8, -6, -14, 0, -19, 14, 4], True)
    test(sln, [0, 0], True)

