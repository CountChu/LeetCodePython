from data_structure import *
import pdb

def test(sln, rowIndex, answer):
    print('rowIndex = %d, answer = %s' % (rowIndex, answer))
    out = sln.getRow(rowIndex)
    assert out == answer, out

def run(sln, module):
    test(sln, 3, [1, 3, 3, 1])
    test(sln, 0, [1])
    test(sln, 1, [1, 1])
