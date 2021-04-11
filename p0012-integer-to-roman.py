import pdb

#
# 4/11: 19 mins, Runtime 48 ms, Memory 14.5 MB
#

class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {
            1: 'I',
            5: 'V',
            4: 'IV',
            9: 'IX',
            10: 'X',    
            40: 'XL',
            90: 'XC',
            50: 'L',
            100: 'C',
            400: 'CD',
            900: 'CM',
            500: 'D',
            1000: 'M',
            }

        num_ls = [*dict]
        num_ls.sort(reverse=True)
        
        idx = 0
        roman = ''
        while True:
            if num < num_ls[idx]:
                idx += 1
                if idx == len(num_ls):
                    break
                continue
 
            v1 = num_ls[idx] 
            roman += dict[v1]
            num = num - v1
 
            #print(idx, v1, num)
        
        
        return roman