
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, n, edges, source, destination, target):
    print("n = %d, edges = %s, source = %d, destination = %d, target = %s" % (
        n, edges, source, destination, target))
    out = sln.validPath(n, edges, source, destination)
    print("out = %s" % out)
    print('')

    assert out == target, out

def run(sln):
    if True:
        test_solution(
            sln, 
            4, 
            [[0, 1], [0, 2], [1, 3], [2, 3]], 
            0, 
            3, 
            True)

    if True:
        test_solution(
            sln, 
            3, 
            [[0, 1], [1, 2], [2, 0]], 
            0, 
            2, 
            True)

    if True:
        test_solution(
            sln, 
            6, 
            [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 
            0, 
            5, 
            False)

    if True:
        test_solution(
            sln, 
            10, 
            [
                [0, 7], [0, 8], [6, 1], [2, 0], [0 ,4],
                [5, 8], [4, 7], [1 ,3], [3, 5], [6, 5]
            ], 
            7, 
            5, 
            True)