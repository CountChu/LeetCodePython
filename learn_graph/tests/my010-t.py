
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
        elif op == 'str':
            out = str(obj)
            assert out == answer
        else :
            assert False, op        

        obj.dump()

    return obj

def run(sln):
    if False:
        obj = test_module(
            sln.module,
            [
                ('UnionFind',  [10],  None),
                # 0 1-2-5-6-7 3-8-9 4
                ('union',      [1, 2],  None),
                ('union',      [2, 5],  None),
                ('union',      [5, 6],  None),
                ('union',      [6, 7],  None),
                ('union',      [3, 8],  None),
                ('union',      [8, 9],  None),
                ('connected',  [1, 5],  True),
                ('connected',  [5, 7],  True),
                ('connected',  [4, 9],  False),
                ## 0 1-2-5-6-7 3-8-9-4
                ('union',      [9, 4],  None),
                ('connected',  [4, 9],  True),
                ('str',        [], '[0, 1, 1, 3, 3, 1, 1, 1, 3, 3]'),
            ]
        )

    #
    # Coursera - Alg P1 - W1.2 Quick Union
    #

    if True:                                 
        obj = test_module(
            sln.module,
            [
                ('UnionFind',  [10],  None),

                ('union',      [3, 4],  None),
                ('str',        [], '[0, 1, 2, 3, 3, 5, 6, 7, 8, 9]'),

                ('union',      [8, 3],  None),
                ('str',        [], '[0, 1, 2, 8, 3, 5, 6, 7, 8, 9]'),

                ('union',      [5, 6],  None),
                ('str',        [], '[0, 1, 2, 8, 3, 5, 5, 7, 8, 9]'),

                ('union',      [4, 9],  None),
                ('str',        [], '[0, 1, 2, 8, 8, 5, 5, 7, 8, 8]')

                ('union',      [1, 2],  None),
                ('union',      [0, 5],  None),
                ('union',      [2, 7],  None),
                ('str',        [], '[0, 1, 1, 8, 8, 0, 5, 1, 8, 8]'),

                ('union',      [1, 6],  None),
                ('union',      [3, 7],  None),
                ('str',        [], '[1, 8, 1, 8, 8, 0, 0, 1, 8, 8]'),
            ]
        )         



