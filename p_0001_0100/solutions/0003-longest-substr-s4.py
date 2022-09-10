from typing import List
import pdb


solution_json = {
    "date": "2021/4/20",
    "coding": 10,
    "runtime": "56 ms",
    "memory": "15.8 MB"
}

class Solution:
    def lengthOfLongestSubstring(self, s):
        debug = False

        max = 0
        s1 = ''
        n = len(s)
        for i in range(n):
            c = s[i]
            if c not in s1:
                s1 += c
            else:   
                if s1[0] == c:
                    s1 = s1[1:]
                else:
                    idx = s1.find(c)
                    s1 = s1[idx+1:]
                    #pdb.set_trace()
                    #s1 = ''
                s1 += c

            if max < len(s1):
                max = len(s1)   

            if debug:
                print(i, c, s1)

        if max < len(s1):
            max = len(s1)   

        return max
