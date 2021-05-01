from typing import List
import pdb

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#
# 2021/5/1: 5 mins, 9 mins, 36 ms, 15.8 MB
#        

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        d = False

        if root == None:
            return []

        out = []
        def travel(node):
            if node == None:
                return

            if node.val != None:
                out.append(node.val)    
            if d:
                print(node.val)
            travel(node.left)
            travel(node.right)

        travel(root)  
        return out

    def transform_ls(self, nums):
        d = False

        out = []
        v = nums
        n = len(v)
        null_ls = []
        count = 0
        for i in range(n):
            if v[i] == None:
                null_ls.append(i)
                null_ls.append(i * 2 + 1)
                null_ls.append(i * 2 + 2)
            else:
                count += 1

        count += len(null_ls)        
        if d:
            print('null_ls = %s, count = %d' % (null_ls, count))

        out = [None] * count            

        j = 0
        for i in range(n):
            if v[i] != None:
                while True:
                    if j in null_ls:
                        j += 1
                    else:
                        break
                out[j] = v[i]  
                j += 1

        if d:
            print('out = %s' % out)

        return out


    def ls_to_tree(self, nums):

        root = TreeNode()
        build_node(root, 8, 8)

        n = len(nums)
        if n == 0:
            return None

        root = TreeNode(nums[0])
        for i in range(n):
            node = build_node(root, i, nums[i])
        
        return root

    def tree_to_ls(self, root):
        ls = []

        node = root
        queue = [node]
        while True:
            if queue == []:
                break
            node = queue.pop(0)
            ls.append(node.val)

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

        return ls

def build_node(root, idx, val):

    path = get_path(idx)
    node = root
    for i in range(len(path)):
        if path[i] == 'l':
            if node.left == None:
                node.left = TreeNode()
            node = node.left

        elif path[i] == 'r':
            if node.right == None:
                node.right = TreeNode()
            node = node.right

        else:
            assert False, path[i]

        if i == len(path) - 1:
            node.val = val

    return node


def get_path(idx):
    path = []

    while True:
        if idx == 0:
            break

        if idx % 2 == 0:
            path.insert(0, 'r')
            idx = (idx - 2) / 2
        else:
            path.insert(0, 'l')
            idx = (idx - 1) / 2

    return path
