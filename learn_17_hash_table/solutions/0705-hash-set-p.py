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
    "date": "2022/9/19",
    "design": 0,
    "coding": 0,
    "runtime": "469 ms",
    "fasterThan": "40%",
    "memory": "18.8 MB" 
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
        n = 100 
        self.b = [[] for _ in range(n) ]                  # bucket. 

    def cal_idx(self, x):
        y = x % len(self.b)
        return y

    def find_key(self, key):
        idx = self.cal_idx(key)
        values = self.b[idx]
        found = False
        for v in values:
            if v == key:
                found = True
        return idx, found

    def __str__(self):
        return '%s' % self.b

    def dump(self):
        print(str(self))   

    def add(self, key: int) -> None:
        idx, found = self.find_key(key)

        if not found: 
            self.b[idx].append(key)

    def remove(self, key: int) -> None:
        idx, found = self.find_key(key)

        if found:
            self.b[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx, found = self.find_key(key)
        return found

