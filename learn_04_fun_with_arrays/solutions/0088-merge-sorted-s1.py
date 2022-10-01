# 
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# 
# The number of elements initialized in nums1 and nums2 are m and n respectively. 
# You may assume that nums1 has a size equal to m + n 
# such that it has enough space to hold additional elements from nums2
# 

from typing import List
import pdb

solution_json = {
    "date": "2021/3/27",
    "runtime": "36 ms",
    "memory": "14.3 MB"
}

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #print('nums1 = %s, nums2 = %s' % (nums1, nums2))
        out = [0] * (m + n)
        idx1 = 0 # for nums1
        idx2 = 0 # for nums2
        idx3 = 0
        while True:
            #line = ''

            if idx1 < m:
                num1 = nums1[idx1]
            else:
                num1 = None

            if idx2 < n:
                num2 = nums2[idx2]
            else:
                num2 = None

            if idx1 >= m and idx2 >= n:
                break

            #line += 'nums1[%d] = %d, nums2[%d] = %d, ' % (idx1, num1, idx2, num2)
            
            if num1 != None and num2 != None:
            
                if num1 < num2:
                    min = num1
                    idx1 += 1
                else:
                    min = num2
                    idx2 += 1

            elif num1 == None and num2 != None:
                min = num2
                idx2 += 1
                
            elif num2 == None and num1 != None:
                min = num1
                idx1 += 1

            #line += 'min = %d' % min
            out[idx3] = min
            idx3 += 1
            #print(line)
        for i in range(m + n):
            nums1[i] = out[i]
            
        
def test(sln, nums1, m, nums2, n, target):
    out = nums1.copy()
    sln.merge(out, m, nums2, n)
    #pdb.set_trace()
    print('nums1 = %s, m = %d, num2 = %s, n = %d, out = %s' % (nums1, m, nums2, n, out))
    assert out == target
        
"""        
sln = Solution()
test(sln, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
test(sln, [1], 1, [], 0, [1])
"""