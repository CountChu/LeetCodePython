from typing import List
import pdb

solution_json = {
    "date": "2021/4/22",
    "coding": 13,
    "runtime": "8720 ms",
    "memory": "17.1 MB"
}

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = False

        n = len(nums)
        pre = None
        i = 0
        while True:
            if i == n:
                break
            num = nums[i]

            if d:
                print(i, pre, num)

            if pre != None and pre == num:
                for j in range(i+1, n):
                    nums[j-1] = nums[j]
                n -= 1                  

                if d:
                    print('nums = %s' % nums)

            else:
                i += 1

            pre = num

        return n