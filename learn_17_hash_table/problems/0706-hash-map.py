#
# https://leetcode.com/problems/design-hashmap/
#
# Design a HashMap without using any built-in hash table libraries.
#
# Implement the MyHashMap class:
#   MyHashMap() 
#       initializes the object with an empty map.
#   void put(int key, int value) 
#       inserts a (key, value) pair into the HashMap. If the key already exists 
#       in the map, update the corresponding value.
#   int get(int key) 
#       returns the value to which the specified key is mapped, or -1 
#       if this map contains no mapping for the key.
#   void remove(key) 
#       removes the key and its corresponding value if the map contains the mapping 
#       for the key.
#
# Example 1:
#       Input
#           ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
#           [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
#       Output
#           [null, null, null, 1, -1, null, 1, null, -1]
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
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
#

class MyHashMap:
    def __init__(self):
        pass

    def __str__(self):
        return ''

    def dump(self):
        print(str(self))        

    def put(self, key: int, value: int) -> None:
        pass

    def get(self, key: int) -> int:
        return 0

    def remove(self, key: int) -> None:
        pass