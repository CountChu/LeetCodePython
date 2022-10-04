from data_structure import *
import pdb

def test(sln, s, target):
    print("s = %s, target = %s" % (s, target))
    sln.heapify(s)
    #print("s = %s" % s)
    assert s == target, s

def run(sln):
    test(sln, [12, 9, 10, 6, 4, 5, 3], [3, 4, 5, 6, 9, 12, 10])
