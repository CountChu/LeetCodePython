# 
# An integer is a palindrome when it reads the same backward as forward. 
# For example, 121 is palindrome while 123 is not.
# 

import pdb

solution_json = {
    "date": "2021/4/11",
    "coding": 6,
    "runtime": "103 ms",
    "fasterThan": "45.67%",
    "memory": "13.8 MB"
}    

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
            
        for i in range(len(num_ls) // 2):
            #print(i, n-i)
            if num_ls[i] != num_ls[-1-i]:
                return False
        return True      