from data_structure import *
import pdb

def test(sln, module, op_ls, data_ls, answer_ls):
    print('op_ls = %s, data_ls = %s, answer_ls = %s' % (op_ls, data_ls, answer_ls))

    for op, data, answer in zip(op_ls, data_ls, answer_ls):        
        if op == 'BSTIterator':
            root = binary_tree_v3.ls_to_tree(data[0])
            it = module.BSTIterator(root)
            assert None == answer, None
        elif op == 'next':
            val = it.next()
            assert val == answer, val
        elif op == 'hasNext':
            flag = it.hasNext()
            assert flag == answer, flag
        else:
            assert False, op

def run(sln, module):
    test(
        sln, 
        module,
        ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
        [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []],
        [None, 3, 7, True, 9, True, 15, True, 20, False]
        )
