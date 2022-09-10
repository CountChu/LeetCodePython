from data_structure import *
import pdb

def test(sln, mat, answer):
    print('mat = %s, answer = %s' % (mat, answer))
    out = sln.updateMatrix(mat)
    assert out == answer, out

def run(sln, module):
    if True:
        test(
            sln, 
            [[0,0,0],
             [0,1,0],
             [0,0,0]], 
            [[0,0,0],
             [0,1,0],
             [0,0,0]],
            )

    if True:
        test(
            sln,
            [[0,0,0],
             [0,1,0],
             [1,1,1]],
            [[0,0,0],
             [0,1,0],
             [1,2,1]],
            )

    if True:
        test(
            sln,
            [[0,0,0],
             [0,1,1],
             [1,1,1]],
            [[0,0,0],
             [0,1,1],
             [1,2,2]],
            )        

    if True:
        test(
            sln,
            [[0,0,1,1],
             [0,0,1,1],
             [0,1,0,1],
             [1,1,0,0]],
            [[0,0,1,2],
             [0,0,1,2],
             [0,1,0,1],
             [1,1,0,0]],
            )         
