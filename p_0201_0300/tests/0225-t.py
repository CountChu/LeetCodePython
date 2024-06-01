from data_structure import *
import pdb

def test(module, script_ls):
    for script in script_ls:
        print(script)    
        op, data, answer = script 

        if op == 'MyStack':
            obj = module.MyStack()
        elif op == 'push':
            obj.push(data[0])
        elif op == 'pop':
            out = obj.pop()
        elif op == 'top':
            out = obj.top()
            assert out == answer, out
        elif op == 'empty':
            out = obj.empty()
            assert out == answer
        else:
            assert False, op

def run(sln):
    test(
        sln.module, 
        [
            ["MyStack",  [],     None],
            ["push",     [1],    None], 
            ["push",     [2],    None],
            ["top",      [],     2], 
            ["pop",      [],     2], 
            ["empty",    [],     False],
        ]
        )
