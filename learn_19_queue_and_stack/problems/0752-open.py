#
# https://leetcode.com/problems/open-the-lock/
#
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: 
# '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
# The wheels can rotate freely and wrap around: 
# for example we can turn '9' to be '0', or '0' to be '9'. 
# Each move consists of turning one wheel one slot.
#
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
#
# You are given a list of deadends dead ends, meaning if the lock displays any 
# of these codes, the wheels of the lock will stop turning 
# and you will be unable to open it.
#
# Given a target representing the value of the wheels that will unlock the lock, 
# return the minimum total number of turns required to open the lock, or -1 
# if it is impossible.
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

    def openLock(self, deadends: List[str], target: str) -> int:
        pass
