from data_structure import *
import pdb

def test(sln, n, answer):
    print('n = %d, answer = %d' % (n, answer))
    out = sln.numSquares(n)
    assert out == answer, out

def run(sln):
    test(sln, 12, 3)
    test(sln, 13, 2)
    test(sln, 99, 3)
    test(sln, 6175, 4)
    test(sln, 6665, 3)
    test(sln, 7168, 4)
    test(sln, 7691, 3)
