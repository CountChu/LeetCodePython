
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, edges, target):
    print("edges = %s, target = %s" % (edges, target))
    out = sln.topologicalSort(edges)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(
        sln, 
        [
            ('A', 'B'),
            ('A', 'C'),
            ('B', 'D'),
            ('C', 'B'),
            ('C', 'D'),
        ],
        ['A', 'C', 'B', 'D']
    ),
    
    test_solution(
        sln, 
        [
            ('1', '0'),
            ('2', '0'),
            ('3', '1'),
            ('3', '2'),
        ],
        ['3', '1', '2', '0']
    )    
