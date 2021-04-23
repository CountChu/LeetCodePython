# 
# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of the list, 
# and each element in the array contains a single digit.
# 
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# 

from typing import List
import pdb

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        #print('digits = %s' % digits)
        for i in reversed(range(len(digits))):
            #line = ''
            #line += 'digits[%d] = %d,' % (i, digits[i])
            if digits[i] == 10:
                digits[i] = 0
                if i >= 1:
                    digits[i-1] += 1
                else:
                    digits.insert(0, 1)
                    break
            #print(line)
        return digits