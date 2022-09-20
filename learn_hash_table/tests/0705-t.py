
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

        if op == 'MyHashSet':
            obj = module.MyHashSet()

        elif op == 'add':
            obj.add(data[0])

        elif op == 'contains':
            out = obj.contains(data[0])
            assert out == answer

        elif op == 'remove':
            obj.remove(data[0])

        else :
            assert False, op        

        obj.dump()

    return obj

def run(sln):
    if True:
        obj = test_module(
            sln.module,
            [
                ('MyHashSet',  [],   None),
                ('add',        [1],  None),
                ('add',        [2],  None),
                ('contains',   [1],  True),
                ('contains',   [3],  False),
                ('add',        [2],  None),
                ('contains',   [2],  True),
                ('remove',     [2],  None),
                ('contains',   [2],  False),
            ]
        )
