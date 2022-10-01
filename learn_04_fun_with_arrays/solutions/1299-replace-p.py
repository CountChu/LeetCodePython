#
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
#
# Given an array arr, replace every element in that array with the greatest 
# element among the elements to its right, and replace the last element 
# with -1.
#
#  After doing so, return the array.
#
# Example 1:
#       Input: arr = [17, 18, 5, 4, 6, 1]
#       Output: [18, 6, 6, 6, 1, -1]
#
# Example 2:
#       Input: arr = [400]
#       Output: [-1]
#


from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/1",
    "design": 0,
    "coding": 0,
    "runtime": "1360 ms",
    "fasterThan": "31%",
    "memory": "15.5 MB" 
}

class Solution:

    '''
          0
        [17, 18, 5, 4, 6, 1]
              1
        [18, 18, 5, 4, 6, 1]        
                 2
        [18,  6, 5, 4, 6, 1]
                    3
        [18,  6, 6, 4, 6, 1]
                       4  
        [18,  6, 6, 6, 6, 1]
                          5
        [18,  6, 6, 6, 1, 1]

        [18,  6, 6, 6, 1, -1]
    '''

    def replaceElements(self, arr: List[int]) -> List[int]:
        ls = sorted(arr, reverse=True)
        out = []
        for i, v in enumerate(arr):
            ls.remove(v)
            if len(ls) == 0:
                max_v = -1 
            else:
                max_v = ls[0]
            #print(max_v)
            out.append(max_v)

        return out
