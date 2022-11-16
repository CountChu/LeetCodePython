
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, matrix, target):
    print("matrix = %s, target = %s" % (matrix, target))
    sln.setZeroes(matrix)
    out = matrix
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    if 1 == 1:
        test_solution(
            sln,

            [[1,1,1],
             [1,0,1],
             [1,1,1]], 
            
            [[1,0,1],
             [0,0,0],
             [1,0,1]])

    if 1 == 1:
        test_solution(
            sln,

            [[0, 1, 2, 0],
             [3, 4, 5, 2],
             [1, 3, 1, 5]],
            
            [[0, 0, 0, 0],
             [0, 4, 5, 0],
             [0, 3, 1, 0]])








