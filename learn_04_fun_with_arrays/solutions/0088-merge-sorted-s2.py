from typing import List
import pdb

solution_json = {
    "date": "2021/4/25",
    "design": 19,
    "coding": 16,
    "runtime": "60 ms",
    "memory": "15.5 MB"
}

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        def insert(nums, m, pos, v):
            if m == len(nums):
                nums.append(0)
            for i in range(len(nums)-1, pos-1, -1):
                if i == pos:
                    nums[i] = v
                else:
                    nums[i] = nums[i-1]

            #pdb.set_trace()
            m += 1
            return m    


        d = False
        i = 0
        j = 0

        while True:
            if d:
                print(i, j)

            if i == m and j == n:
                break

            elif i == m:
                m = insert(nums1, m, i, nums2[j])
                i += 1
                j += 1    
                if d:
                    print('                 ', i, j, m, nums1)                

            elif j == len(nums2):
                break

            elif nums1[i] < nums2[j]:
                i += 1
            else:
                m = insert(nums1, m, i, nums2[j])
                j += 1
                if d:
                    print('                 ', i, j, m, nums1)
                

