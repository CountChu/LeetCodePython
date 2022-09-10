from data_structure import *
import pdb

def test(sln, module, op_ls, data_ls, answer_ls):
    print('op_ls = %s, data_ls = %s, answer_ls = %s' % (op_ls, data_ls, answer_ls))
    
    for op, data, answer in zip(op_ls, data_ls, answer_ls):
        print(op, data, answer)
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

def run(sln, module):
    test(
        sln, 
        module,
        ["MyStack", "push", "push", "top", "pop", "empty"],
        [[], [1], [2], [], [], []],
        [None, None, None, 2, 2, False])


'''
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        

    def top(self) -> int:
        """
        Get the top element.
        """
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
'''    