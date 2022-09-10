from data_structure import *
import pdb

def test(sln, module, op_ls, data_ls, answer_ls):
    print('op_ls = %s, data_ls = %s, answer_ls = %s' % (op_ls, data_ls, answer_ls))
    
    for op, data, answer in zip(op_ls, data_ls, answer_ls):
        print(op, data, answer)
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

def run(sln, module):
    test(
        sln, 
        module,
        ["MyQueue", "push", "push", "peek", "pop", "empty"],
        [[], [1], [2], [], [], []],
        [None, None, None, 1, 1, False])

'''
class Solution:
    def __init__(self):
        pass

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
'''