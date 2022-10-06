from data_structure import *
import pdb
br = pdb.set_trace

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def ls_to_tree(ls):
    d = False

    if ls == []:
        return None

    nd_ls = []
    for v in ls:
        nd = Node(v)
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

    out_ls = []

    #pdb.set_trace()
    q = [root]
    while True:
        if q == []:
            break

        n = q.pop(0)
        if d:
            print(n.val)

        out_ls.append(n.val)
        if n.next == None:
            out_ls.append('#')

        if n.left != None:
            q.append(n.left)

        if n.right != None:
            q.append(n.right)

    #pdb.set_trace()
    return out_ls

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    root = ls_to_tree(nums)

    out = sln.connect(root)
    out_ls = tree_to_ls(out)
    assert out_ls == answer, out_ls


def run(sln):
    if True:
        test(
            sln, 
            [1, 2, 3, 4, 5, None, 7], 
            [1, '#', 2, 3, '#', 4, 5, 7, '#'])

    if True:
        test(sln, [], [])
    
    if True:
        test(
            sln, 
            [1,2,None,3,None,4,None,5], 
            [1,'#',2,'#',3,'#',4,'#',5,'#'])

    if True:
        test(
        	sln, 
        	[1, 2, 3, 4, 5, 6, 7, None, None, 8, 9],
        	[1, '#', 2, 3, '#', 4, 5, 6, 7, '#', 8, 9, '#'])
