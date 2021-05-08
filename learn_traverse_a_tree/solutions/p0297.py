from typing import List
import pdb

#
# 2021/5/4: 5, 28, 168 ms, 20.4 MB
#

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    def serialize(self, root):
        d = False

        if root == None:
            return ''

        ls = []

        q = [root]
        last_idx = -1
        while True:
            if q == []:
                break

            n = q.pop(0)
            if d:
                if n == None:
                    print('N')
                else:
                    print(n.val)

            if n == None:
                ls.append('N')
            else:
                ls.append(str(n.val))
                last_idx = len(ls) - 1

            if n == None:
                continue

            if n.left == None:
                q.append(None)
            else:
                q.append(n.left)

            if n.right == None:
                q.append(None)
            else:
                q.append(n.right)

        ls = ls[:last_idx+1]
        data = ','.join(ls)
        return data  

    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    def deserialize(self, data):
        d = False
        if data == '':
            return None

        #pdb.set_trace()
        ls = data.split(',')
        v = int(ls.pop(0))
        root = TreeNode(v)
        q = [root]
        while True:
            if ls == []:
                break

            n = q.pop(0)
            if d:
                if n == None:
                    print(None)
                else:
                    print(n.val)
            if n == None:
                continue

            left_v = ls.pop(0)
            if left_v == 'N':
                left = None
            else:
                left = TreeNode(int(left_v))
                n.left = left

            q.append(left)
            if d:
                print(' ' * 8, 'left_v = ', left_v)

            if ls == []:
                break

            right_v = ls.pop(0)
            if right_v == 'N':
                right = None
            else:
                right = TreeNode(int(right_v))
                n.right = right

            q.append(right)
            if d:
                print(' ' * 8, 'right_v = ', right_v)

        return root


Solution = Codec
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
