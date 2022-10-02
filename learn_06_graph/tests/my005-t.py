
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
                ('UnionFind',  [9],  None),
                ('str',        [], '[-1, -1, -1, -1, -1, -1, -1, -1, -1]'),
                                  #   0   1   2   3   4   5   6   7   8

                ('union',      [1, 2],  None),
                ('str',        [], '[-1, -2, 1, -1, -1, -1, -1, -1, -1]'),
                                  #   0   1  2   3   4   5   6   7   8

                ('union',      [3, 4],  None),
                ('str',        [], '[-1, -2, 1, -2, 3, -1, -1, -1, -1]'),

                ('union',      [5, 6],  None),
                ('str',        [], '[-1, -2, 1, -2, 3, -2, 5, -1, -1]'),

                ('union',      [7, 8],  None),
                ('str',        [], '[-1, -2, 1, -2, 3, -2, 5, -2, 7]'),

                ('union',      [2, 4],  None),
                ('str',        [], '[-1, -4, 1, 1, 3, -2, 5, -2, 7]'),

                ('union',      [2, 5],  None),
                ('str',        [], '[-1, -6, 1, 1, 3, 1, 5, -2, 7]'),

                ('connected',  [1, 3],  True),
                ('union',      [6, 8],  None),
                ('connected',  [5, 7],  True),
                ('str',        [], '[-1, -8, 1, 1, 3, 1, 5, 1, 7]'),
            ]
        ) 
