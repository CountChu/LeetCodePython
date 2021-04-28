from typing import List
import pdb

#
# 2021/4/25: 8 mins, 72 ms, 15.6 MB
#

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def get_digits(v1):
            v2 = 1
            while True:
                if v1 < 10:
                    break                
                v2 += 1
                v1 = v1 // 10

            #pdb.set_trace()
            return v2


        d = False
        n = len(nums)

        out = 0
        for i in range(n):
            v1 = nums[i]
            v2 = get_digits(v1)
            if v2 % 2 == 0:
                out += 1
            if d:
                print(i, v1, v2)

        #pdb.set_trace() 
        return out       
