from data_structure import *
import pdb

def test_module(module, script_ls):
    for script in script_ls:
        print(script)
        op, data, answer = script

        if op == 'BSTIterator':
            root = binary_tree_v3.ls_to_tree(data[0])
            obj = module.BSTIterator(root)
            assert None == answer, None
        elif op == 'next':
            val = obj.next()
            assert val == answer, val
        elif op == 'hasNext':
            flag = obj.hasNext()
            assert flag == answer, flag
        else:
            assert False, op

        obj.dump()

def run(sln):
    if True:
        obj = test_module(
            sln.module,
            [
                ("BSTIterator", [[7, 3, 15, None, None, 9, 20]], None),
                ("next",        [], 3),
                ("next",        [], 7),
                ("hasNext",     [], True),
                ("next",        [], 9),
                ("hasNext",     [], True),
                ("next",        [], 15),
                ("hasNext",     [], True),
                ("next",        [], 20),
                ("hasNext",     [], False),
            ]
        )
