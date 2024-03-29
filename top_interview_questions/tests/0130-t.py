
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, board, target):
    print("board = %s, target = %s" % (board, target))
    sln.solve(board)
    out = board
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    
    if False:
        test_solution(
            sln, 

            [["X","X","X","X"],
             ["X","O","O","X"],
             ["X","X","O","X"],
             ["X","O","X","X"]], 
            
            [["X","X","X","X"],
             ["X","X","X","X"],
             ["X","X","X","X"],
             ["X","O","X","X"]])

    if False:
        test_solution(
            sln, 

            [["X"]], 
            
            [["X"]])

    if False:
        test_solution(
            sln, 

            [["O","X","O","O","X","X"],
             ["O","X","X","X","O","X"],
             ["X","O","O","X","O","O"],
             ["X","O","X","X","X","X"],
             ["O","O","X","O","X","X"],
             ["X","X","O","O","O","O"]], 
            
            [["O","X","O","O","X","X"],
             ["O","X","X","X","O","X"],
             ["X","O","O","X","O","O"],
             ["X","O","X","X","X","X"],
             ["O","O","X","O","X","X"],
             ["X","X","O","O","O","O"]])

    if True:
        test_solution(
            sln, 

            [["O","X","O"],
             ["X","O","X"],
             ["O","X","O"]], 
            
            [["O","X","O"],
             ["X","X","X"],
             ["O","X","O"]])






