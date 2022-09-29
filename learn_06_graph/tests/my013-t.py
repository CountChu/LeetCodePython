
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, start, edges, target):
    print("start = %d, edges = %s, target = %s" % (start, edges, target))
    v_d = sln.bellman(start, edges)
    print("v_d = %s" % v_d)
    print('')

    assert v_d == target

def run(sln):

    #
    # AB - Alg - 4.4 Bellman
    #

    if True:
        test_solution(
            sln, 
            1,
            [
                (1, 2, 6), 
                (1, 3, 5), 
                (1, 4, 5), 
                (2, 5, -1), 
                (3, 2, -2), 
                (3, 5, 1), 
                (4, 3, -2), 
                (4, 6, -1), 
                (5, 7, 3), 
                (6, 7, 3)
            ],
            {
                1: 0, 
                2: 1, 
                3: 3, 
                4: 5, 
                5: 0, 
                6: 4,
                7: 3,
            }
        )

