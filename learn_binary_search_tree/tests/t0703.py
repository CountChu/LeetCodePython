from data_structure import *
import pdb

def test(sln, module, op_ls, data_ls, answer_ls):
    print('op_ls = %s, data_ls = %s, answer = %s' % (op_ls, data_ls, answer_ls))
    
    for op, data, answer in zip(op_ls, data_ls, answer_ls):
        if op == 'KthLargest':
            obj = module.KthLargest(data[0], data[1])
            assert None == answer, None
    
        elif op == 'add':
            out = obj.add(data[0])
            assert out == answer, out
    
        else:
            assert(op, False)

def run(sln, module):

    if True:
        test(
            sln, 
            module,
            ["KthLargest", "add", "add", "add", "add", "add"],
            [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
            [None, 4, 5, 5, 8, 8],
            )

    if True:
        test(
            sln,
            module,
            ["KthLargest","add","add","add","add","add"],
            [[1,[]],[-3],[-2],[-4],[0],[4]],
            [None, -3, -2, -2, 0, 4], 
            )

    if True:
        test(
            sln,
            module,
            ["KthLargest","add","add","add","add","add"],
            [[3,[5,-1]], [2], [1], [-1], [3], [4]],
            [None, -1, 1, 1, 2, 3],
            )