from typing import List
import pdb

#
# 2021/4/22: 46 mins, runtime: 92 ms, memory: 15.9 MB
#

d = False

def str_to_ls(s):
    ls = [c for c in s]
    return ls

def ls_to_str(ls):
    str = ''
    for v in ls:
        str += v
    return str 

def gen(ls):
    d = False
    if d:
        print('ls = %s' % ls)
    pair = '()'
    s_ls = []
    for i in range(len(ls)+1):
        ls1 = ls.copy()
        ls1.insert(i, pair)
        s = ls_to_str(ls1)
        if d:
            print(i, s)
        if s not in s_ls:
            s_ls.append(s)

    return s_ls

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        global d

        s_ls = ['()']
        count = 1
        while True:
            if count >= n:
                break

            s_ls3 = []
            #pdb.set_trace()
            for s in s_ls:
                if d:
                    print(s_ls)
                ls = str_to_ls(s)
                s_ls2 = gen(ls)
                for s2 in s_ls2:
                    if s2 not in s_ls3:
                        s_ls3.append(s2)
            count += 1
            #pdb.set_trace()


            s_ls = s_ls3

        return s_ls
                
