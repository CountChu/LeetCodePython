from data_structure import *
import pdb

def test(sln, deadends, target, answer):
    print('deadends = %s, target = %s, answer = %s' % (deadends, target, answer))
    out = sln.openLock(deadends, target)
    assert out == answer, out

def run(sln):
    test(sln, ["0201", "0101", "0102", "1212", "2002"], "0202", 6)
    test(sln, ["8888"], "0009", 1)
    test(sln, ["0000"], "8888", -1)
    test(sln, ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888", -1)
