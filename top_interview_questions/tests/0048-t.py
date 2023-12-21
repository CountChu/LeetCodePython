
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, matrix, target):
    print("matrix = %s, target = %s" % (matrix, target))
    sln.rotate(matrix)
    out = matrix
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):

    if 1==0:
        test_solution(
            sln,

            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]], 
            
            [[7, 4, 1],
             [8, 5, 2],
             [9, 6, 3]])

    if 1==0:
        test_solution(
            sln, 

            [[ 5,  1,  9, 11],
             [ 2,  4,  8, 10],
             [13,  3,  6,  7],
             [15, 14, 12, 16]], 
            
            [[15, 13,  2,  5],
             [14,  3,  4,  1],
             [12,  6,  8,  9],
             [16,  7, 10, 11]])

    if 0 == 0:
        test_solution(
            sln, 

            [[ 1,  2,  3,  4,  5],
             [ 6,  7,  8,  9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]],

            [[21, 16, 11,  6, 1],
             [22, 17, 12,  7, 2],
             [23, 18, 13,  8, 3],
             [24, 19, 14,  9, 4],
             [25, 20, 15, 10, 5]])


