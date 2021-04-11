# 
# Given an input string (s) and a pattern (p), 
# implement regular expression matching with support for '.' and '*' where: 
# 
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# 
 

import pdb

#
# 4/10: 1 hr.
#

class Solution(object):

    #
    # Top-Down Variation
    #

    def isMatch(self, s, p):
        reg = []
        state = 'init'
        log = False
        for c in p:
            
            if state == 'init' and c != '*':
                state = 'ch'
            elif state == 'init' and c == '*':
                assert False
            elif state == 'ch' and c == '*':
                state = '*'
            elif state == 'ch' and c != '*':
                state = 'ch'
            elif state == '*' and c != '*':
                state = 'ch'
            else:
                assert False
            
            if state == 'ch':
                reg.append([c, '1'])
            elif state == '*':
                idx = len(reg) - 1
                reg[idx][1] = '*'

        m = len(s)
        n = len(reg)

        f = {}
        for i in reversed(range(0, m + 1)):
            for j in reversed(range(0, n + 1)):
                matched, is_star = is_match(s, i, reg, j)
                
                if not is_star:
                    if not matched:
                        f[(i, j)] = False
                    else:
                        if i == m and j == n:
                            f[(i, j)] = True
                        else:        
                            f[(i, j)] = f[(i + 1, j + 1)]
                
                else:
                    if not matched:
                        f[(i, j)] = f[(i, j + 1)]
                    else:
                        if i == m:
                            f[(i, j)] = f[(i, j + 1)]
                        elif j == n:
                            f[(i, j)] = f[(i + 1, j)]
                        else:
                            f[(i, j)] = f[(i + 1, j)] or f[(i, j + 1)]

                if log:
                    print(i, j, f[(i, j)])   
                
        return f[(0, 0)]            

def is_match(s, i, reg, j):
    if i == len(s) and j == len(reg):
        return True, False
    elif i == len(s):
        if reg[j][1] == '*':
            return True, True
        else:    
            return False, False
    elif j == len(reg):
        return False, False
    elif i < len(s):
        if reg[j][0] == '.':
            return True, reg[j][1] == '*'
        else:    
            if s[i] == reg[j][0]:
                return True, reg[j][1] == '*'
            else:
                return False, reg[j][1] == '*'
    else:
        assert false