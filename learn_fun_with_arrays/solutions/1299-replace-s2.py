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
#       Input: arr = [17,18,5,4,6,1]
#       Output: [18,6,6,6,1,-1]
#
# Example 2:
#       Input: arr = [400]
#       Output: [-1]
#


from typing import List
import pdb

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "4621 ms",
    "fasterThan": "27%",
    "memory": "16.9 MB" 
}

br = pdb.set_trace

class Solution:
    

    def replaceElements(self, arr: List[int]) -> List[int]:
        order = sorted(arr, reverse=True)
        size = len(arr)
        for i in range(size):
            order.remove(arr[i])
            if order == []:
                arr[i] = -1
            else:
                arr[i] = max(order)

        return arr

