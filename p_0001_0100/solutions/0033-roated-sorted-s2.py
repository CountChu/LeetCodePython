solution_json = {
    "date": "2023/12/13",
    "design": 0,
    "coding": 82,
    "runtime": "58 ms",
    "fasterThan": "7%",
    "memory": "16.85 MB"
}

#
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated 
# at an unknown pivot index k (1 <= k < nums.length) such that the resulting 
# array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 
# and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
          0 1 2 3 4 5 6 7
         [4 5 6 7 8 1 2 3]  target 8
          l     m       r
                l   m   r
                l   r 

          0 1 2 3 4 5 6
         [4 5 6 7 0 1 2]  target 0
          l     m     r
                l     r

          0 1 2 3 4 5 6
         [4 5 6 7 0 1 2]  target 3
          l     m     r

           0 1
          [1 3] 0

           0 1 2
          [3 5 1] 3
           l m r 

         0 1 2
        [1 3 5]
         l m r

         0 1 2
        [5 1 3] 0
         l m r


'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        out = -1
        while True:
            if nums[r] == target:
                out = r
                break

            if nums[l] == target:
                out = l 
                break

            if l == r:
                break

            if r - l == 1:
                break

            m = (l + r) // 2
            #lg(l, m, r)

            if nums[m] == target:
                out = m
                break

            #
            #  0 1 2 3 4 5 6 7
            # [4 5 6 7 8 1 2 3]  target 8
            #  l     m       r
            #
            #  0 1 2 3 4 5 6
            # [4 5 6 7 0 1 2]  target 0
            #  l     m     r
            #

            if nums[r] < nums[l] < nums[m]:
                if nums[l] < target < nums[m]:
                    r = m 
                else:
                    l = m 

            #
            #    0 1 2 
            #   [5 1 3]
            #    l m r
            #
            #    0 1 2 3 4 5 6 7
            #   [4 5 6 7 8 1 2 3]  target 8
            #          l   m   r         
            #
            #    0 1 2 3 4
            #   [5 1 2 3 4]
            #    l   m   r   
            #

            elif nums[m] < nums[r] < nums[l]:
                if nums[m] < target < nums[r]:
                    l = m
                else:
                    r = m

            elif nums[l] < nums[m] < nums[r]:
                if nums[l] < target < nums[m]:
                    r = m
                elif nums[m] < target < nums[r]:
                    l = m
                else:
                    break

            else:
                #br()
                pass

        return out











     
