
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, s, target):
    print("s = %s, target = %s" % (s, target))
    out = sln.func(s)
    print("out = %s" % out)
    print('')

    assert out == target

def test_module(module, script_ls):
    for script in script_ls:
        print(script)
        op, data, answer = script

        if op == 'UnionFind':
            obj = module.UnionFind(data[0])
        elif op == 'init':
            obj.init(data)
        elif op == 'union':
            obj.union(data[0], data[1])
        elif op == 'connected':
            out = obj.connected(data[0], data[1])
            assert out == answer 
        elif op == 'get_w':
            out = obj.get_w()
            assert out == answer, out
        elif op == 'get_a':
            out = obj.get_a()
            assert out == answer, out
        else :
            assert False, op        

        obj.dump()

    return obj

def run(sln):
    if True:
        obj = test_module(
            sln.module,
            [
                ('UnionFind',  [10],  None),
                ('union',      [4, 3],  None),
                ('get_w',      [], [1, 1, 1, 1, 2, 1, 1, 1, 1, 1]),
                ('get_a',      [], [0, 1, 2, 4, 4, 5, 6, 7, 8, 9]),
                                  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

                ('union',      [3, 8],  None),
                ('get_w',      [], [1, 1, 1, 1, 2, 1, 1, 1, 1, 1]),
                ('get_a',      [], [0, 1, 2, 4, 4, 5, 6, 7, 4, 9]),

                ('union',      [6, 5],  None),

                ('union',      [9, 4],  None),
                ('union',      [2, 1],  None),
                ('get_w',      [], [1, 1, 2, 1, 2, 1, 2, 1, 1, 1]),
                ('get_a',      [], [0, 2, 2, 4, 4, 6, 6, 7, 4, 4]),

                ('union',      [5, 0],  None),
                ('union',      [7, 2],  None),
                ('union',      [6, 1],  None),
                ('union',      [7, 3],  None),
                ('get_w',      [], [1, 1, 2, 1, 2, 1, 3, 1, 1, 1]),
                ('get_a',      [], [6, 2, 6, 4, 6, 6, 6, 2, 4, 4])
                                  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
            ]
        )
