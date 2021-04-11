# 
# An integer is a palindrome when it reads the same backward as forward. 
# For example, 121 is palindrome while 123 is not.
# 

import pdb

#
# 2021/4/11: 6 mins, Runtime: 72ms, Memory: 14.3 MB
#

class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        if x < 0:
            return False
    
        num_ls = []
        while True:
            v1 = x % 10
            x = x // 10
            #print(x, v1)
            num_ls.append(v1)
            if x == 0:
                break
            
        n = len(num_ls)
        #print(n)
        flag = True
        for i in range(n//2):
            #print(i, n-i)
            if num_ls[i] != num_ls[n-1-i]:
                flag = False
                break
        return flag        