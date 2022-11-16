
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, intervals, target):
    print("intervals = %s, target = %s" % (intervals, target))
    out = sln.merge(intervals)
    print("out = %s" % out)
    print('')

    assert out == target


def run(sln):
    if 1 == 1:
        test_solution(
            sln, 
            [[1, 3], [2, 6], [8, 10], [15, 18]], 
            [[1, 6], [8, 10], [15, 18]])
    
    if 1 == 1:
        test_solution(
            sln, 
            [[1, 4], [4, 5]], 
            [[1, 5]])

    if 1 == 1:
        test_solution(
            sln, 
            [[1, 3]], 
            [[1, 3]])

    if 1 == 1:
        test_solution(
            sln,
            [[1, 4], [0, 5]],
            [[0, 5]])

    if 1 == 1:
        test_solution(
            sln,
            [[1, 4], [0, 2], [3, 5]],
            [[0, 5]])

    if 1 == 1:
        test_solution(
            sln,
            [[2, 3], [4, 6], [5, 7], [3, 4]],
            [[2, 7]])

    if 1 == 1:
        test_solution(
            sln,
            [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]],
            [[2, 4], [5, 5]])




