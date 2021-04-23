import pdb

#
# 4/11: 7 mins, Runtime: 44 ms, Memory: 14.3 MB
#

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
            }
        
        idx = 0
        out = 0
        while True:
            symbol = s[idx:idx+2]
            if symbol in dict:
                v1 = dict[symbol]
                out += v1
                idx += 2
            else:    
                symbol = s[idx]
                v1 = dict[symbol]
                out += v1
                idx += 1
                
            #print(symbol, v1, out)
                
            if idx >= len(s):
                break
                    
        return out
        