
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, s, t, target):
    print("s = %s, t = %s, target = %s" % (s, t, target))
    out = sln.isAnagram(s, t)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, 'anagram', 'nagaram', True)
    test_solution(sln, 'rat', 'car', False)
