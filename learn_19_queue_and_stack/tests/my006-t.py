from data_structure import *
import pdb

def test(module, script_ls):
    for script in script_ls:
        print(script)
        op, data, answer = script

        if op == 'Stack':
            obj = module.Stack()
        elif op == 'push':
            obj.push(data[0])
        elif op == 'pop':
            obj.pop()
        elif op == 'top':
            out = obj.top()
            assert out == answer, out

        obj.dump()

    return obj

def run(sln):
    obj = test(
        sln.module,
        [
            ('Stack',    [],   None), 
            ('push',     [-2], None), 
            ('push',     [0],  None), 
            ('push',     [-3], None), 
            ('pop',      [],   None), 
            ('top',      [],   0), 
            ('push',     [1], None), 
            ('top',      [],   1), 

        ]
    )