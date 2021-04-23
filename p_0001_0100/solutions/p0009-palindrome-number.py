# 
# An integer is a palindrome when it reads the same backward as forward. 
# For example, 121 is palindrome while 123 is not.
# 

import pdb

#
# 2021/4/3: 5 mins
#

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #print('x = %d' % x)
        
        if x < 0:
            return False
            
        ls1 = []
        while True:
            v1 = x % 10
            x = x // 10
            ls1.append(v1)
            #print(v1, x)
            if x == 0:
                break
                
        ls2 = []
        for i in reversed(range(len(ls1))):
            ls2.append(ls1[i])
        
        return ls1 == ls2