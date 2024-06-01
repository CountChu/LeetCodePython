from data_structure import *
import pdb

def test(sln, tokens, answer):
    print('tokens = %s, answer = %d' % (tokens, answer))
    out = sln.evalRPN(tokens)
    assert out == answer, out

def run(sln):
    test(sln, ["2", "1", "+", "3", "*"], 9)
    test(sln, ["4", "13", "5", "/", "+"], 6)
    test(sln, ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)

