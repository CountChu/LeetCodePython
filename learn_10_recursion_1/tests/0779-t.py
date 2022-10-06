from data_structure import *
import pdb

def test(sln, n, k, answer):
    print('n = %d, k = %d, answer = %d' % (n, k, answer))
    out = sln.kthGrammar(n, k)
    assert out == answer, out

'''
    n = 4        1 2 3 4 5 6 7 8
        row 1    0
        row 2    0 1
        row 3    0 1 1 0
        row 4    0 1 1 0 1 0 0 1
'''
def run(sln):
    test(sln, 1, 1, 0)
    test(sln, 2, 1, 0)
    test(sln, 2, 2, 1)
    test(sln, 4, 5, 1)
    test(sln, 4, 6, 0)
    test(sln, 4, 7, 0)

