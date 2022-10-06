#
# https://leetcode.com/problems/unique-binary-search-trees-ii/
#
# Given an integer n, return all the structurally unique BST's (binary search trees), 
# which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
#
# Example 1:
#       Input: n = 3
#       Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#
# Example 2: 
#       Input: n = 1
#       Output: [[1]]
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/6",
    "design": 0,
    "coding": 0,
    "runtime": "55 ms",
    "fasterThan": "96%",
    "memory": "15.8 MB" 
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def generateTrees(self, n: int) -> List[TreeNode]:
        v_ls = [i for i in range(1, n + 1)]
        nd_ls = gen_3(v_ls)
        return nd_ls

    def test(self, n: int) -> List[TreeNode]:

        if n == 1:
            nd_ls = gen_1([1])

        elif n == 2:
            nd_ls = gen_2([1, 2])
        
        elif n == 3:
            nd_ls = gen_3([1, 2, 3])

        else:
            nd_ls = []

        return nd_ls


def gen_1(v_ls):
    return [TreeNode(v_ls[0])]

def gen_2(v_ls):
    out = []

    nd1 = TreeNode(v_ls[0])
    nd2 = TreeNode(v_ls[1])
    nd1.right = nd2
    out.append(nd1)

    nd1 = TreeNode(v_ls[0])
    nd2 = TreeNode(v_ls[1])
    nd2.left = nd1
    out.append(nd2)

    return out

def gen_3(v_ls):
    if len(v_ls) == 1:
        return gen_1(v_ls)

    if len(v_ls) == 2:
        return gen_2(v_ls)

    out = []
    for i in range(len(v_ls)):
        v_ls_ls = split(v_ls, i)
        
        if i == 0:
            v = v_ls_ls[0][0]
            nd_ls = gen_3(v_ls_ls[1])
            for nd in nd_ls:
                nd0 = TreeNode(v)
                nd0.right = nd
                out.append(nd0)

        elif i == len(v_ls) - 1:
            v = v_ls_ls[1][0]
            nd_ls = gen_3(v_ls_ls[0])
            for nd in nd_ls:
                nd0 = TreeNode(v)
                nd0.left = nd 
                out.append(nd0)

        else:
            v = v_ls_ls[1][0]

            nd_ls1 = gen_3(v_ls_ls[0])
            nd_ls2 = gen_3(v_ls_ls[2])

            for nd1 in nd_ls1:
                for nd2 in nd_ls2:
                    nd0 = TreeNode(v)
                    nd0.left = nd1
                    nd0.right = nd2
                    out.append(nd0)

        print(v_ls_ls)

    return out

'''
        v
    [0, 1, 2, 3, 4, 5, 6, 7]
'''
def split(v_ls, idx):
    if idx == 0:
        v_ls_0 = [v_ls[0]]
        v_ls_1 = v_ls[1:]
        return [v_ls_0, v_ls_1]

    elif idx == len(v_ls) - 1:
        v_ls_0 = v_ls[:idx]
        v_ls_1 = [v_ls[idx]]
        return [v_ls_0, v_ls_1]

    else:
        v_ls_0 = v_ls[:idx]
        v_ls_1 = [v_ls[idx]]
        v_ls_2 = v_ls[idx+1:]
        return [v_ls_0, v_ls_1, v_ls_2]













