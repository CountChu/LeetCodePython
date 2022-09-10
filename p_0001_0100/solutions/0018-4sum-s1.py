from typing import List
import pdb

solution_json = {
    "date": "2021/4/17",
    "coding": 27,
    "runtime": "1704 ms",
    "memory": "15.7 MB"           
}

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        debug = False

        out_ls = []

        nums.sort()
        if debug:
            print('nums = %s, target = %d' % (nums, target))    

        n = len(nums)
        seen = {}
        for i in range(n - 3):
            v = nums[i]
            if v in seen:
                continue
            seen[v] = i

            v2 = target - v
            if debug:
                print(i, v, v2)

            three_sum_ls = self.threeSum(nums[i+1:], v2)
            for three_sum in three_sum_ls:
                out = [v] + three_sum
                out_ls.append(out)

        #pdb.set_trace()
        return out_ls

    def threeSum(self, nums, target):
        debug = False

        out_ls = []

        if debug:
            print('nums = %s, target = %d' % (nums, target))

        n = len(nums)
        seen = {}
        for i in range(n - 2):
            v = nums[i]
            if v in seen:
                continue
            seen[v] = i
            
            v2 = target - v
            if debug:
                print(i, v, v2)

            two_sum_ls = self.twoSum(nums[i+1:], v2)    
            for two_sum in two_sum_ls:
                out = [v] + two_sum
                out_ls.append(out)

        return out_ls

    def twoSum(self, nums, target):
        debug = False

        out_ls = []

        if debug:
            print('nums = %s, target = %d' % (nums, target))

        n = len(nums)
        seen = {}
        j = n - 1
        for i in range(n - 1):
            v = nums[i]
            if v in seen:
                continue
            seen[v] = i
            
            if debug:
                print(i, v)

            out = None
            while True:

                if i >= j:
                    break

                v2 = nums[j]
                if v + v2 == target:
                    out = [v, v2]
                    break
                elif v + v2 > target:
                    j -= 1
                else:
                    break

            if out != None:
                out_ls.append(out)        

        return out_ls











