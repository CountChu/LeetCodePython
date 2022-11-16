from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2021/4/17",
    "coding": 46,
    "runtime": "1060 ms",
    "fasterThan": "87%",    
    "memory": "17.8 MB"
}   


class Solution:
    def threeSum(self, nums):
        nums.sort()
        #print('nums = %s' % nums)
        
        n = len(nums)
        out_ls = []
        seen = {}
        for i in range(n-2):
            v = nums[i]
            if v in seen:
                continue
            seen[v] = i
                
            v2 = -v
            two_sum_ls = self.twoSum(nums[i+1:], v2)
            for two_sum in two_sum_ls:
                out = [v] + two_sum
                #print(i, out)
                out_ls.append(out)

        return out_ls

    def twoSum(self, nums, target):
        #print('nums = %s, target = %d' % (nums, target))
        n = len(nums)
        j = n - 1
        out_ls = []
        seen = {}
        for i in range(n - 1):
            if nums[i] in seen:
                continue
            seen[nums[i]] = i   

            if i >= j:
                break            

            out = None
            while True:
                sum = nums[i] + nums[j]
                if sum == target:
                    out = [nums[i], nums[j]]
                    break
                elif sum > target:    
                    j -= 1
                else:
                    break

                if i == j:
                    break

            if out != None:
                #print('i = %d, j = %d, out = %s' % (i, j, out))
                out_ls.append(out)
                #pdb.set_trace()        
        return out_ls
