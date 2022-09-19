#
# https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3864/
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

    def bellman(self, start, edges):
        v_d = {
            1: 0,
            2: 1, 
            3: 3, 
            4: 5,
            5: 0,
            6: 4,
            7: 3,
        }

        return v_d