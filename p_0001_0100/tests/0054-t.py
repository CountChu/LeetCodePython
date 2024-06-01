
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

    if True:
        test_solution(
            sln, 

            [[1,  2,  3,  4],
             [5,  6,  7,  8],
             [9, 10, 11, 12]],

            [1,2,3,4,8,12,11,10,9,5,6,7])


    if True:
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

    if True:
        test_solution(
            sln, 

            [[7],
             [9],
             [6]],

            [7,9,6])


    if True:
        test_solution(
            sln,

            [[1]],
              
            [1])

    
    if True:
        test_solution(
            sln,

            [[3],
             [2]],
              
            [3, 2])


    if True:
        test_solution(
            sln, 
            
            [[1,2,3],
             [4,5,6],
             [7,8,9]], 

            [1,2,3,6,9,8,7,4,5])

    if True:
        test_solution(
            sln,

            [[1,2,3,4,5,6,7,8,9,10],
             [11,12,13,14,15,16,17,18,19,20]],

            [1,2,3,4,5,6,7,8,9,10,20,19,18,17,16,15,14,13,12,11])


