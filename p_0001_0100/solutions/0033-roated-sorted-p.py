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

solution_json = {
    "date": "2022/11/7",
    "design": 0,
    "coding": 0,
    "runtime": "59 ms",
    "fasterThan": "78",
    "memory": "14.5 MB" 
}


'''
         0  1  2  3  4  5  6  7
        [5, 6, 7, 0, 1, 2, 3, 4]
         i        k           j
         i  k     j
            i  k  j  

               v
         5  6  7  0  1  2  3  4
         0  1  2  3  4  5  6  7
        [5, 6, 7, 0, 1, 2, 3, 4]


         0  1  2  3  4  5  6  7
        [0, 1, 2, 3, 4, 5, 6, 7], target = 2
         .                    .
         .        .
            .     .
               .

         0  1  2  3  4  5  6
        [0, 1, 2, 4, 5, 6, 7], target = 3
         i        k        j
         i  k     j
            i  k  j
               i  j


         0  1  2  3  4  5  6
        [6, 7, 1, 2, 3, 4, 5]
         i        k        j




'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        max_idx = find_max(nums)
        #print('max_idx = %d' % max_idx)

        i = 0
        n = len(nums)
        j = n - 1

        while True:
            if j - i == 1:
                org_i = org_idx(i, max_idx, n)
                v = nums[org_i]
                if v == target:
                    return org_i

                org_j = org_idx(j, max_idx, n)
                v = nums[org_j]
                if v == target:
                    return org_j

                break

            k = (i + j) // 2
            #print(i, j, k)

            org_k = org_idx(k, max_idx, n)
            v = nums[org_k]

            if v == target:
                return org_k
            
            elif v < target:
                i = k 
            
            else:
                j = k         

        #br()
        return -1

        
def find_max(nums):
    i = 0
    n = len(nums)
    j = n - 1
    if nums[i] > nums[j]:               # It is rotated
        return find_max_in_rotated(nums)
    else:
        return j

'''
         0  1  2  3  4  5  6  7
        [4, 5, 6, 7, 8, 1, 2, 3]
         i        k           j
'''        

def find_max_in_rotated(nums):
    i = 0
    n = len(nums)
    j = n - 1
    
    while True:
        #print(i, j)
        if j - i <= 1:
            break

        k = (i + j) // 2
        if nums[i] < nums[k]:
            i = k
        elif nums[k] < nums[j]:
            j = k 
        else:
            assert False 

    if nums[i] < nums[j]:
        return j
    else:
        return i

def org_idx(idx, max_idx, n):
    return (max_idx + idx + 1) % n



     
