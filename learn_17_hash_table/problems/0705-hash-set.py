#
# https://leetcode.com/problems/design-hashset/
#
# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
#   void add(key) 
#       Inserts the value key into the HashSet.
#   bool contains(key)
#       Returns whether the value key exists in the HashSet or not.
#   void remove(key) 
#       Removes the value key in the HashSet. If key does not exist in the HashSet, 
#       do nothing.
#
#
# Example 1:
#       Input: 
#           [
#               "MyHashSet", "add", "add", "contains", "contains", 
#               "add", "contains", "remove", "contains"
#           ],
#           [
#               [], [1], [2], [1], [3], 
#               [2], [2], [2], [2]
#           ]
#
#       Output: 
#           [
#               null, null, null, true, false, 
#               null, true, null, false
#           ] 
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def findNumbers(self, nums: List[int]) -> int:
        return 0

#
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)        
#

class MyHashSet:
    def __init__(self):
        pass

    def __str__(self):
        return ''

    def dump(self):
        print(str(self))   

    def add(self, key: int) -> None:
        pass        

    def remove(self, key: int) -> None:
        pass

    def contains(self, key: int) -> bool:
        return True

