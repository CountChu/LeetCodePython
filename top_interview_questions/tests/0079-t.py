
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, board, word, target):
    print("board = %s, word = %s, target = %s" % (board, word, target))
    out = sln.exist(board, word)
    print("out = %s" % out)
    print('')

    assert out == target


def run(sln):
    if True:
        test_solution(
            sln, 
            
            [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]], 
            
            "ABCCED",

            True)

    if True:
        test_solution(
            sln,

            [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]],

            "SEE", 

            True)


    if True:
        test_solution(
            sln,

            [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]],

            "ABCB",

            False)

    if True:
        test_solution(
            sln,

            [["a"]],

            "a",

            True)

    if True:
        test_solution(
            sln, 

            [["a", "b"],
             ["c", "d"]],

             "acdb",

             True)

    if True:
        test_solution(
            sln, 

            [["a", "b"],
             ["c", "d"]],

             "cdba",

             True)

    if True:
        test_solution(
            sln, 

            [["A","A","A","A","A","A"],
             ["A","A","A","A","A","A"],
             ["A","A","A","A","A","A"],
             ["A","A","A","A","A","A"],
             ["A","A","A","A","A","B"],
             ["A","A","A","A","B","A"]], 

             "AAAAAAAAAAAAABB",

             False)




