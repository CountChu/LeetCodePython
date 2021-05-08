import pdb

#
# 2021/5/4: 29 mins, 30 mins
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def ls_to_tree(ls):
    d = False

    if ls == []:
        return None

    nd_ls = []
    for v in ls:
        nd = TreeNode(v)
        nd_ls.append(nd)

    root = nd_ls.pop(0)
    q = [root]

    while True:
        if nd_ls == []:
            break

        nd = q.pop(0)
        if d:
            print(nd.val)

        if nd.val != None:

            left = nd_ls.pop(0)
            if d:
                print(' '*8, 'left =', left.val)   

            if left.val != None:
                nd.left = left

            q.append(left)

            if nd_ls == []:
                break
             

            right = nd_ls.pop(0)
            if d:
                print(' '*8, 'right', right.val)    

            if right.val != None:
                nd.right = right

            q.append(right)

    #pdb.set_trace()
    return root

def tree_to_ls(root):
    d = False

    if root == None:
        return []

    out = []
    q = [root]
    last_idx = -1
    while True:
        if q == []:
            break

        n = q.pop(0)
        if d:
            if n != None:
                print(n.val)
            else:
                print(None)

        if n != None:
            out.append(n.val)
            last_idx = len(out) - 1
        else:
            out.append(None)    

        if n == None:
            continue

        if n.left != None:
            q.append(n.left)
        else:
            q.append(None)

        if n.right != None:
            q.append(n.right)
        else:
            q.append(None)

    out = out[:last_idx+1]
    return out






