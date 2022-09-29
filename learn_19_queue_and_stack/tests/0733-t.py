from data_structure import *
import pdb

def test(sln, image, sr, sc, newColor, answer):
    print('image = %s, sr = %d, sc = %d, newColor = %d, answer = %s' % (image, sr, sc, newColor, answer))
    out = sln.floodFill(image, sr, sc, newColor)
    assert out == answer, out

def run(sln, module):

    if True:
        test(
            sln,
            [[1,1,1],
             [1,1,0],
             [1,0,1]],
            1,
            1,
            2,
            [[2,2,2],
             [2,2,0],
             [2,0,1]]
            )

    if True:
        test(
            sln, 
            [[0,0,0],[0,0,0]],
            0,
            0,
            2,
            [[2,2,2],[2,2,2]]
            )
