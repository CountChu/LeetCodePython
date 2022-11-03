
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, columnTitle, target):
    print("columnTitle = %s, target = %s" % (columnTitle, target))
    out = sln.titleToNumber(columnTitle)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, 'A', 1)
    test_solution(sln, 'AB', 28)
    test_solution(sln, 'ZY', 701)

