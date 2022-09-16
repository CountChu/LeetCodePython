
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
            assert out == answer
        elif op == 'get_a':
            out = obj.get_a()
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
                # 0 1-2-5-6-7 3-8-9 4
                ('union',      [1, 2],  None),
                ('union',      [2, 5],  None),

                ('union',      [5, 6],  None),
                ('get_a',      [], [0, 1, 1, 3, 4, 1, 1, 7, 8, 9]),
                
                ('union',      [6, 7],  None),
                ('union',      [3, 8],  None),
                ('union',      [8, 9],  None),
                ('get_a',      [], [0, 1, 1, 3, 4, 1, 1, 1, 3, 3]),

                ('connected',  [1, 5],  True),
                ('connected',  [5, 7],  True),
                ('connected',  [4, 9],  False),
                ## 0 1-2-5-6-7 3-8-9-4
                ('union',      [9, 4],  None),
                ('get_w',      [], [1, 2, 1, 2, 1, 1, 1, 1, 1, 1]),                                
                ('get_a',      [], [0, 1, 1, 3, 3, 1, 1, 1, 3, 3]),                
                ('connected',  [4, 9],  True),
            ]
        )



