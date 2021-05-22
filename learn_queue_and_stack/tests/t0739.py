from data_structure import *
import pdb

def test(sln, temperatures, answer):
    print('temperatures = %s, answer = %s' % (temperatures, answer))
    out = sln.dailyTemperatures(temperatures)
    assert out == answer, out

def run(sln, module):
    if True:
        test(
            sln, 
            [73, 74, 75, 71, 69, 72, 76, 73], 
            [1, 1, 4, 2, 1, 1, 0, 0]
            )

    if True:
        test(
            sln,
            [55,38,53,81,61,93,97,32,43,78],
            [3,1,1,2,1,1,0,1,1,0]
            )