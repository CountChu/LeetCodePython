from data_structure import *
import pdb

def test(module, script_ls):
    for script in script_ls:
        print(script)
        op, data, answer = script 
    
        if op == 'MyQueue':
            obj = module.MyQueue()
        elif op == 'push':
            obj.push(data[0])
        elif op == 'pop':
            out = obj.pop()
            assert out == answer, out
        elif op == 'peek':
            out = obj.peek()
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
            ["MyQueue",  [],     None],
            ["push",     [1],    None],
            ["push",     [2],    None],
            ["peek",     [],     1],
            ["pop",      [],     1],
            ["empty",    [],     False],
        ])

