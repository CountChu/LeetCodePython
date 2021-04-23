# 
# Given an input string (s) and a pattern (p), 
# implement regular expression matching with support for '.' and '*' where: 
# 
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# 
 

import pdb

class Solution(object):

    #
    # Top-Down Variation
    #

    def isMatch1(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                print(i, j, ans)
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

    #
    # Bottom-Up Variation
    #

    def isMatch2(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True
        #dumpDp(dp, len(pattern)+1, len(text)+1)
        print('----')


        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
                print(i, j, dp[i][j])    

        return dp[0][0]
        
def dumpDp(dp, m, n):
    for i in range(m):
        for j in range(n):
            print(i, j, dp[i][j])