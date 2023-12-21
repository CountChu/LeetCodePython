
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, matrix, target):
    print("matrix = %s, target = %s" % (matrix, target))
    out = sln.spiralOrder(matrix)
    print("out = %s" % out)
    print('')

    assert out == target, out

def run(sln):

    if 1 == 1:
        test_solution(
            sln, 

            [[1,  2,  3,  4],
             [5,  6,  7,  8],
             [9, 10, 11, 12]],

            [1,2,3,4,8,12,11,10,9,5,6,7])


    if 1 == 1:
        test_solution(
            sln, 

            [[1],
             [2],
             [3],
             [4],
             [5],
             [6],
             [7],
             [8],
             [9],
             [10]],

            [1,2,3,4,5,6,7,8,9,10])    

    if 1 == 1:
        test_solution(
            sln, 

            [[7],
             [9],
             [6]],

            [7,9,6])


    if 1 == 1:
        test_solution(
            sln,

            [[1]],
              
            [1])

    
    if 1 == 1:
        test_solution(
            sln,

            [[3],
             [2]],
              
            [3, 2])


    if 1 == 1:
        test_solution(
            sln, 
            
            [[1,2,3],
             [4,5,6],
             [7,8,9]], 

            [1,2,3,6,9,8,7,4,5])


