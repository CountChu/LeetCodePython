from typing import List
import pdb

#
# 2021/5/3: Time Limit Exceeded, 10 min, 30 min
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        d = False

        def build_tree(nums, v, p):
            idx = nums.index(v)
            left = nums[:idx]
            right = nums[idx+1:]
            
            left_p = []
            right_p = []
            for i in range(len(p)):
                if p[i] in left:
                    left_p.append(p[i])
                elif p[i] in right:
                    right_p.append(p[i])
                else:
                    assert False
            
            if d:
                print(left, v, right, left_p, right_p)
                
            node = TreeNode(v)

            if len(left) >= 1:
                left_v = left_p[-1]
                left_p = left_p[:-1]
                node.left = build_tree(left, left_v, left_p)

            if len(right) >= 1:
                right_v = right_p[-1]
                right_p = right_p[:-1]
                node.right = build_tree(right, right_v, right_p)


            return node        

        v = postorder[-1]
        p = postorder[:-1].copy()
        root = build_tree(inorder, v, p)

        #pdb.set_trace()
        return root


