from data_structure import *
import pdb

def test(sln, x, n, answer):
    print('x = %f, n = %d, answer = %d' % (x, n, answer))
    out = sln.myPow(x, n)
    assert round(out, 3) == answer, out

def run(sln, module):
	test(sln, 0.44528, 0, 0)
    #test(sln, 2.0, 10, 1024.0)
    #test(sln, 2.1, 3, 9.261)
    #test(sln, 2.0, -2, 0.25)

