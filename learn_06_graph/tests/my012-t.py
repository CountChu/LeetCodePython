
from data_structure import *
import sys
import pdb
br = pdb.set_trace

def test_solution(sln, start, edges, target):
    print("start = %d, edges = %s, target = %s" % (start, edges, target))
    v_d = sln.dijkstra(start, edges)
    print("v_d = %s" % v_d)
    print('')

    assert v_d == target

def run(sln):

    #
    # AB - Alg - 3.6 Dijkstra #1
    #

    if True:
        test_solution(
            sln, 
            1,
            [
                (1, 2, 2), 
                (1, 3, 4), 
                (2, 3, 1), 
                (2, 4, 7), 
                (3, 5, 3), 
                (4, 6, 1), 
                (5, 4, 2), 
                (5, 6, 5)
            ],
            {
                1: 0, 
                2: 2, 
                3: 3, 
                4: 8, 
                5: 6, 
                6: 9
            }
        )

    #
    # AB - Alg - 3.6 Dijkstra #2
    #

    if True:
        test_solution(
            sln, 
            1,
            [
                (1, 2, 50), 
                (1, 4, 10), 
                (1, 3, 45), 
                (2, 3, 10), 
                (2, 4, 15),             
                (3, 5, 30),             
                (4, 1, 10), 
                (4, 5, 15),             
                (5, 2, 20), 
                (5, 3, 35),
                (6, 5, 3)
            ],
            {
                1: 0, 
                2: 45, 
                3: 45, 
                4: 10, 
                5: 25, 
                6: sys.maxsize
            }
        )    