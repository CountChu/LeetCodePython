# 
# An integer is a palindrome when it reads the same backward as forward. 
# For example, 121 is palindrome while 123 is not.
#
# Example 1:
#       Input: x = 121
#       Output: true
#
# Example 2:
#       x = -121
#       Output: false
#
# Example 3:
#       x = 10
#       Output: false
# 

import pdb

solution_json = {
    "date": "2022/8/30",
    "coding": 0,
    "runtime": "?? ms",
    "memory": "?? MB"
}

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
            
        s = ''
        while True:
            c = '%d' % (x % 10)
            s += c
            print(c)
            x = x // 10
            if x == 0:
                break

        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                return False 

        return True
