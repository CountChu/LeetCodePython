#
# https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.  
#

from typing import List
import pdb

solution_json = {
    "date": "2021/4/17",
    "coding": 150,
    "runtime": "86 ms",
    "memory": "16.2 MB"
}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        idx_num_ls = [(i, nums[i]) for i in range(len(nums))] 
        idx_num_ls.sort(key=lambda x: x[1])
        #print(idx_num_ls)

        hash = {}
        def sum(i, j):
            if (i, j) not in hash:
                hash[(i, j)] = idx_num_ls[i][1] + idx_num_ls[j][1]
            return hash[(i, j)]

        i = 0
        j = len(idx_num_ls) - 1
        hit = False
        do_break = False
        while True:

            if sum(i, j) == target:
                hit = True
                do_break = True

            elif sum(i+1, j) == target:
                i += 1                
                hit = True
                do_break = True

            elif sum(i, j-1) == target:       
                j -= 1
                hit = True
                do_break = True

            elif sum(i+1, j) > target:
                j -= 1

            elif sum(i+1, j) < target:
                i += 1     

            print(i, j)

            if do_break:
                break


        if hit: 
            return [idx_num_ls[i][0], idx_num_ls[j][0]]
        else:
            return [-1, -1]    