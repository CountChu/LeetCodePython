from typing import List
import pdb

#
# 2021/4/25: 5 mins, 19 mins, 64 ms, 15.6 MB
#

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        d = False

        def remove(nums, n, pos):
            for i in range(pos, n):
                if i <= n - 2: 
                    nums[i] = nums[i + 1]
            n -= 1
            return n

        if d:
            print('i, v, nums --------> n, v, nums')

        n = len(nums)
        for i in range(n):
            v = nums[i]
            if d:
                print(i, v, nums)

            while True:
                if v == val:
                    n = remove(nums, n, i)   
                    v = nums[i] 
                    if d:
                        print('       ', n, v, nums)
                    #pdb.set_trace()
                else:
                    break 

                if i >= n:
                    break                    

            if i >= n:
                break


        #pdb.set_trace()
        return n