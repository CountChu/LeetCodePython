
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, s, target):
    print("s = %s, target = %s" % (s, target))
    n = int(s, 2)
    out = sln.reverseBits(n)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, '01010000000000000000000000000000', 10)    
    test_solution(sln, '11000000000000000000000000000000', 3)
    test_solution(sln, '00000010100101000001111010011100', 964176192)
    test_solution(sln, '11111111111111111111111111111101', 3221225471)
