
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, rooms, target):
    print("rooms = %s, target = %s" % (rooms, target))
    out = sln.canVisitAllRooms(rooms)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [[1], [2], [3], []], True)
    test_solution(sln, [[1,3], [3,0,1], [2], [0]], False)
    test_solution(sln, [[2,3], [], [2], [1,3]], True)
    test_solution(sln, [[1,3], [1,4], [2,3,4,1], [], [4,3,2]], True)
    test_solution(sln, [[1], [], [0,3], [1]], False)


