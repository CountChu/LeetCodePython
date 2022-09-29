from data_structure import *
import pdb

def test(sln, n, answer):
    print('n = %d, answer = %d' % (n, answer))
    out = sln.numSquares(n)
    assert out == answer, out

def run(sln, module):
    test(sln, 12, 3)
    test(sln, 13, 2)
