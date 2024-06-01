
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, numRows, target):
    print("numRows = %d, target = %s" % (numRows, target))
    out = sln.generate(numRows)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    if True:
        test_solution(
            sln, 
            5, 
            [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]])

    if True:
        test_solution(
            sln, 
            1, 
            [[1]])