from data_structure import *
import pdb

def test_module(module, script_ls):
    for script in script_ls:
        print(script)
        op, data, answer = script
        
        if op == 'KthLargest':
            obj = module.KthLargest(data[0], data[1])
            assert None == answer, None
    
        elif op == 'add':
            out = obj.add(data[0])
            assert out == answer, out
    
        else:
            assert(op, False)

        obj.dump()

def run(sln):

    if True:
        '''
            3,       [4, 5, 8, 2]
                     [8, 5, 4, 2]
            add 3    [8, 5, 4, 3, 2]
            add 5    [8, 5, 5, 4, 3, 2]
        '''
        test_module(
            sln.module,
            [
                ("KthLargest", [3, [4, 5, 8, 2]], None),
                ("add",        [3],  4),
                ("add",        [5],  5),
                ("add",        [10], 5),
                ("add",        [9],  8),
                ("add",        [4],  8),
            ]
        )

    if True:
        test_module(
            sln.module,
            [
                ("KthLargest", [1,[]],  None),
                ("add",        [-3],    -3),
                ("add",        [-2],    -2),
                ("add",        [-4],    -2),
                ("add",        [0],      0),
                ("add",        [4],      4),
            ] 
        )

    if True:
        test_module(
            sln.module,
            [
                ("KthLargest", [3,[5,-1]],  None),
                ("add",        [2],          -1),
                ("add",        [1],           1), 
                ("add",        [-1],          1), 
                ("add",        [3],           2), 
                ("add",        [4],           3),
            ]
        )









