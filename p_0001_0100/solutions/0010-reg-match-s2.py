# 
# Given an input string (s) and a pattern (p), 
# implement regular expression matching with support for '.' and '*' where: 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# 

import pdb

solution_json = {
    "date": "2021/4/10",
    "coding": 60
}

class Solution:
    def isMatch(self, s: str, p: str) -> bool:    
    
        log = False
        reg = []
        state = 'init'
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
        for i in range(-1, m):
            for j in range(-1, n):
                matched, determined, is_star = check_matched(i, s, j, reg)

                if determined:
                    f[(i, j)] = matched

                else:    
                    if is_star:
                        if matched:
                            if i == -1:
                                f[(i, j)] = f[(i, j - 1)]
                            else:    
                                f[(i, j)] = f[(i - 1, j)] or f[(i, j - 1)]
                        else:
                            f[(i, j)] = f[(i, j - 1)]
                    else:
                        f[(i, j)] = f[(i - 1, j - 1)]
                    
                if log:
                    print('%2d, %2d, %5s' % (i, j, f[(i, j)]))
          
        return f[(i, j)]
          
def check_matched(i, s, j, reg):

    is_star = False
    if j >= 0:
        if reg[j][1] == '*':
            is_star = True

    matched = False
    determined = False
    
    if i == -1 and j == -1:
        matched = True
        determined = True
    elif i == -1:
        if is_star:
            matched = True
            determined = False
        else:    
            matched = False
            determined = True
    elif j == -1:
        matched = False
        determined = True
    else:
        if reg[j][0] == '.':
            matched = True
            determined = False
        else:    
            if s[i] == reg[j][0]:
                matched = True
                determined = False
            else:
                matched = False
                if is_star:
                    determined = False
                else:    
                    determined = True
    
    return matched, determined, is_star