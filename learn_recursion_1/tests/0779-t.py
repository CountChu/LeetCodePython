from data_structure import *
import pdb

def test(sln, n, k, answer):
    print('n = %d, k = %d, answer = %d' % (n, k, answer))
    out = sln.kthGrammar(n, k)
    assert out == answer, out

def run(sln, module):
    test(sln, 1, 1, 0)
    test(sln, 2, 1, 0)
    test(sln, 2, 2, 1)
    test(sln, 4, 5, 1)
    test(sln, 4, 6, 0)

