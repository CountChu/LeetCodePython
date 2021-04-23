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
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        def matches(i: int, j:int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for  _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] != f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]

        for i in range(m + 1):
            for j in range(0, n + 1):
                print(i, j, f[i][j])                
                        
        return f[m][n]                    

#
# 2021/4/3: 3 mins.
#

def test(sln, s, p, target):
    print('s = %s, p = %s' % (s, p))
    out = sln.isMatch(s, p)
    print('out = %s' % (out))
    assert out == target        

sln = Solution()

#test(sln, 'aa', 'aaa', False)
#test(sln, 'aaa', 'aaaa', False)
#test(sln, 'aaa', 'baa', False)
#test(sln, 'abb', 'acb', False)
#test(sln, 'aaa', 'a.a', True)
#test(sln, 'aaa', 'b.a', False)
#test(sln, 'aa', 'a', False)
#test(sln, 'ab', '...', False)
#
#test(sln, 'a', '.*..', False)
#test(sln, 'a', '.*.*..', False)
#test(sln, 'a', '.*.*.*..', False)

#test(sln, 'ab', '.*..', True)
#test(sln, 'abcd', 'd*', False)
#test(sln, 'aaa', 'ba*a', False)
#test(sln, 'aab', 'c*a*b', True)
#test(sln, 'aaa', 'a*a', True)   
test(sln, 'aaa', 'aa*a', True)
#
#test(sln, 'abc', 'ba*a', False)
#test(sln, 'abc', 'aa*a', False)
#test(sln, 'aac', 'a*bc', False)
#
#test(sln, 'bac', 'a*bc', False)
#test(sln, 'bac', 'ba*b', False)
#test(sln, 'bac', 'aa*b', False)
#test(sln, 'abc', 'a*bc', True) 
#test(sln, 'aaa', 'a*aa', True)
#test(sln, 'aaa', 'a*.', True)
#test(sln, 'aaab', 'a*ab', True)
#test(sln, 'aaab', 'aa*b', True)
#test(sln, 'aaab', 'a*.', True)
#test(sln, 'ab', '.*c', False)
#test(sln, 'aa', 'a*', True)
#test(sln, 'ab', '.*', True)
#
#test(sln, 'aab', 'ca*b', False)
#test(sln, 'aab', 'c*d*a*b', True)
#test(sln, 'bbbba', '.*a*a', True)
#test(sln, 'a', '.*..a*', False)
#test(sln, 'bbab', 'b*a*', False)
#test(sln, 'a', 'c*.', True)
#test(sln, 'b', 'c*bb', False)
#test(sln, 'aabcbcbcaccbcaabc', '.*a*aa*.*b*.c*.*a*', True) 
#test(sln, 'abbabaaaaaaacaa', 'a*.*b.a.*c*b*a*c*', True) 


#test(sln, '', 'c*', True)
#test(sln, '', '.*', True)
#test(sln, '', '.', False)
#test(sln, 'a', '', False)
#
#test(sln, '', '', True)
#test(sln, '', 'bab', False)
#test(sln, '', 'c*c*', True)
