#
# https://leetcode.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#

from typing import List
import pdb

solution_json = {
    "date": "2021/3/24"
}

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        min_len = None
        for str in strs:
            if len(str) == 0:
                return ""
            if min_len == None:
                min_len = len(str)
            else:
                if len(str) < min_len:
                    min_len = len(str)
    

        prefix = ""
        for i in range(min_len):
            ch = None
            same = True
            for str in strs:
                if ch == None:
                    ch = str[i]
                if ch != str[i]:
                    same = False
                    break
            if same:
                prefix += ch
            else:
                break
        return prefix        
