from typing import List
import pdb

#
# 2021/5/5: 10, 50, 84 ms, 20.1 MB
#

def dump(found):
    p_str = 'None'
    d_str = 'None'
    n_str = 'None'
    
    p = found['p']
    d = found['d']
    n = found['n']

    if p != None:
        p_str = str(p.val)
    if d != None:
        d_str = d
    if n != None:
        n_str = str(n.val)
    return '(%s, %s, %s)' % (p_str, d_str, n_str)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        d = False

        if root == None:
            return None

        #
        # Find the node of the key
        #

        found = {
            'p': None,  # the parent of the found node
            'd': None,  # left or dir
            'n': None,  # the found node
            }

        n = root
        while True:
            if n == None:
                break

            if d:
                print(n.val)

            if n.val == key:
                found['n'] = n
                break

            elif key < n.val:
                found['p'] = n
                found['d'] = 'left'
                n = n.left

            elif key > n.val:
                found['p'] = n
                found['d'] = 'right'
                n = n.right 

        if found['n'] == None:
            return root

        if d:
            print('found = ', dump(found))

        #
        # Case 1. There are not children of the "found".
        #   

        if found['n'].left == None and found['n'].right == None:
            if d:
                print('Case 1:')

            if found['p'] != None:    
                if found['d'] == 'left':
                    found['p'].left = None
                else:
                    found['p'].right = None
            else:
                root = None

            return root

        #
        # Case 2. There is only one child of the "found"
        #

        if found['n'].left == None and found['n'].right != None:
            if d:
                print('Case 2.1:')  
                          

            if found['d'] == 'left':
                found['p'].left = found['n'].right
            elif found['d'] == 'right':
                found['p'].right = found['n'].right
            elif found['d'] == None:
                root = found['n'].right
            else:
                assert False

            return root

        if found['n'].right == None and found['n'].left != None:
            if d:
                print('Case 2.2:')

            if found['d']  == 'left':
                found['p'].left = found['n'].left
            elif found['d'] == 'right':
                found['p'].right = found['n'].left
            elif found['d'] == None:
                root = found['n'].left
            else:
                assert False

            return root


        #
        # Case 3. Here, there are two children of the "found"
        #

        if d:
            print('Case 3:')        

        #
        # Find the leftmost of the found.right
        #

        leftmost = {
            'p': None,  # the parent of the leftmost node
            'd': None,  # left or dir
            'n': None,  # the leftmost node
            }        

        leftmost['p'] = found['n']
        leftmost['d'] = 'right'
        leftmost['n'] = found['n'].right

        while True:

            leftmost_n = leftmost['n'].left

            if leftmost_n == None:
                break

            if d:
                print(leftmost_n.val)                

            leftmost['p'] = leftmost['n']
            leftmost['d'] = 'left'
            leftmost['n'] = leftmost_n

        if d:
            print('leftmost = ', dump(leftmost))

        #
        # Move the value of the leftmost into the found node
        #

        found['n'].val = leftmost['n'].val

        #
        # Remove the leftmost but keep its right child if it has.
        #

        if leftmost['d'] == 'right':
            leftmost['p'].right = leftmost['n'].right
        elif leftmost['d'] == 'left':
            leftmost['p'].left = leftmost['n'].right

        return root


