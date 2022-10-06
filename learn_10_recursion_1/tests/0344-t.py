from data_structure import *
import pdb

def test(sln, s, answer):
    print('s = %s, answer = %s' % (s, answer))
    out = s.copy()
    sln.reverseString(out)
    assert out == answer, out

def run(sln):
    test(sln, ["h","e","l","l","o"], ["o","l","l","e","h"])
    test(sln, ["H","a","n","n","a","h"], ["h","a","n","n","a","H"])
