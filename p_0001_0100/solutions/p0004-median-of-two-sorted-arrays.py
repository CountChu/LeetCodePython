# 
# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.
# 

from typing import List
import pdb

#
# 3/28: 17 mins
#

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #print('nums1 = %s, nums2 = %s' % (nums1, nums2))
        
        #
        # Merge sort.
        #
        
        nums3 = []
        idx1 = 0
        idx2 = 0
        while True:  

            line = ''
            line += 'idx1 = %d, ' % idx1
            line += 'idx2 = %d, ' % idx2
        
            if idx1 < len(nums1) and idx2 < len(nums2):
                num1 = nums1[idx1]
                num2 = nums2[idx2]
                if num1 < num2:
                    idx1 += 1
                    nums3.append(num1)
                else:
                    idx2 += 1
                    nums3.append(num2)
            
            elif idx1 < len(nums1) and idx2 >= len(nums2):
                num1 = nums1[idx1]
                idx1 += 1
                nums3.append(num1)
            
            elif idx1 >= len(nums1) and idx2 < len(nums2):
                num2 = nums2[idx2]
                idx2 += 1
                nums3.append(num2)
                        
            #print(line)

            if idx1 == len(nums1) and idx2 == len(nums2):
                break
                
        #
        # Find median
        #
        
    
        if len(nums3) % 2 == 1:
            idx = len(nums3) // 2
            m = nums3[idx]
        else:
            idx1 = len(nums3) // 2
            idx0 = idx1 - 1
            m = (nums3[idx0] + nums3[idx1]) / 2
            
        return m    

        

        




