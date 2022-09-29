from data_structure import *
import pdb

def test(sln, n, answer):
    print('n = %d, answer = %d' % (n, answer))
    out = sln.fib(n)
    assert out == answer, out

def run(sln, module):
    test(sln, 2, 1)
    test(sln, 3, 2)
    test(sln, 4, 3)


