import pdb

#
# 2021/5/1: 
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def transform_ls(nums):
    d = False

    v = nums
    n = len(v)
    null_ls = []
    count = 0
    for i in range(n):
        if v[i] == None:
            null_ls.append(i)
            null_ls.append(i * 2 + 1)
            null_ls.append(i * 2 + 2)
            count += 3
        else:
            count += 1


    if d:
        print('null_ls = %s, count = %d' % (null_ls, count))

    out = [None] * count
    j = 0
    last_idx = -1
    for i in range(n):
        if v[i] != None:
            while True:
                if j in null_ls:
                    j += 1
                else:
                    break
            out[j] = v[i]     
            last_idx = j
            j += 1

    if d:
        print('out = %s, last_idx = %d' % (out, last_idx))

    out = out[:last_idx+1]
    return out

def ls_to_tree(nums):
    d = False

    v = nums
    if v == []:
        return None

    n = {}      # i ---> node
    for i in range(len(v)):
        if v[i] != None:
            n[i] = TreeNode(v[i])

    if d:
        print(n.keys())

    for i in n:
        left = i * 2 + 1
        if left in n:
            n[i].left = n[left]

        right = i * 2 + 2
        if right in n:
            n[i].right = n[right]

    root = n[0]

    return root

def tree_to_ls(root):
    d = True

    if root == None:
        return []

    q = [(root, 0)]
    n = {}   # idx ---> node

    while True:
        if q == []:
            break

        node, idx = q.pop(0)
        n[idx] = node.val

        if node.left != None:
            left = idx * 2 + 1
            q.append((node.left, left))

        if node.right != None:
            right = idx * 2 + 2
            q.append((node.right, right))

    if d:
        print('n = %s' % n)

    out = [None] * (max(n) + 1)
    for idx in n:
        out[idx] = n[idx]

    return out



