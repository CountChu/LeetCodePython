#
# https://leetcode.com/problems/implement-stack-using-queues/
#
# Implement a last-in-first-out (LIFO) stack using only two queues. 
# The implemented stack should support all the functions of a normal stack 
# (push, top, pop, and empty).
#
# Implement the MyStack class:
#   void push(int x) Pushes element x to the top of the stack.
#   int pop() Removes the element on the top of the stack and returns it.
#   int top() Returns the element on the top of the stack.
#   boolean empty() Returns true if the stack is empty, false otherwise.
#
# Notes:
#   You must use only standard operations of a queue, which means 
#   that only push to back, peek/pop from front, size and is empty operations 
#   are valid.
#
#   Depending on your language, the queue may not be supported natively. 
#   You may simulate a queue using a list or deque (double-ended queue) 
#   as long as you use only a queue's standard operations.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/29",
    "design": 0,
    "coding": 0,
    "runtime": "63 ms",
    "fasterThan": "20%",
    "memory": "14.1 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]
'''
    push(1)     1 ->
    push(2)     1 -> 2 ->
    top()       2
    pop()       
'''

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def get_last(head):
    nd = head 
    last = None
    while nd != None:
        if nd.next == None:
            last = nd 
        nd = nd.next
    return last

def dump(head):
    if head == None:
        print('None')

    s = ''
    nd = head
    while nd != None:
        s += '%d -> ' % nd.val 
        nd = nd.next
    print(s)

def queue_push(head, x):
    nd = Node(x)
    if head == None:
        head = nd 
    else:
        last_nd = get_last(head)
        last_nd.next = nd 
    return head

def queue_pop(head):
    if head == None:
        return None, None

    first = head
    head = head.next
    return head, first

def queue_empty(head):
    return head == None

class MyStack:

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        self.head = queue_push(self.head, x)

    def pop(self) -> int:
        last = None
        head2 = None
        nd2 = None
        while self.head != None:
            self.head, first = queue_pop(self.head)
            if first != None and first.next == None:
                last = first 
            else:
                head2 = queue_push(head2, first.val)

        self.head = head2

        if last == None:
            return None
        else:
            return last.val

        
    def top(self) -> int:
        last_nd = get_last(self.head)
        if last_nd == None:
            return None 
        else:
            return last_nd.val
        
    def empty(self) -> bool:
        return queue_empty(self.head)







