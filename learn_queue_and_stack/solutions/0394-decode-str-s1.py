from typing import List
import pdb

solution_json = {
    "date": "2021/6/22",
    "design": 21,
    "coding": 17,
    "runtime": "20 ms",
    "memory": "15.9 MB"
}  

class Solution:
    def decodeString(self, s: str) -> str:
        d = False
        n = len(s)        

        flag = 'init' # 1, a, [, ] 
        number = ''
        word = ''
        ls = []
        for i in range(n):
            if flag == 'init':
                if s[i].isnumeric():
                    flag = '1'
                elif s[i] == '[':
                    flag = '['
                elif s[i] == ']':
                    flag = ']'
                else:
                    flag = 'a'
            elif flag == '1':
                if s[i].isnumeric():
                    flag = '1'
                elif s[i] == '[':
                    flag = '['
                elif s[i] != ']':
                    flag = 'a'
                else:
                    assert False, s[i]
            elif flag == '[':
                if s[i].isnumeric():
                    flag = '1'
                elif s[i] == '[':
                    assert False, s[i]
                elif s[i] == ']':
                    assert False, s[i]
                else:
                    flag = 'a'
            elif flag == ']':
                if s[i].isnumeric():
                    flag = '1'
                elif s[i] == '[':
                    assert False, s[i]
                elif s[i] == ']':
                    flag = ']'
                else:
                    flag = 'a'
            elif flag == 'a':
                if s[i].isnumeric():
                    flag = '1'
                elif s[i] == '[':
                    assert False, s[i]
                elif s[i] == ']':
                    flag = ']'
                else:
                    flag = 'a'

            if d:
                print('s[%d] = %s, flag = %s' % (i, s[i], flag))

            if flag == '1':
                number = number + s[i]
                if word != '':
                    ls.append(word)
                    word = ''
            elif flag == 'a':
                word = word + s[i]
                if number != '':
                    ls.append(number)
                    number = ''
            elif flag in ['[', ']']:
                if word != '':
                    ls.append(word)
                    word = ''
                if number != '':
                    ls.append(number)
                    number = ''
                ls.append(s[i])
            else:
                assert False, flag

        if word != '':
            ls.append(word)

        if d:
            print('ls = %s' % ls)

        n = len(ls)
        stack = []
        for i in range(n):
            v = ls[i]
            if d:
                print('%d: %s' % (i, v))
        
            if v != ']':
                stack.append(v)
            else:
                handle_stack(stack)

            if d:
                print('    stack = %s' % stack)

        out = ''
        while True:
            if stack == []:
                break
            v = stack.pop()
            out = v + out

        return out

def handle_stack(stack):
    flag = 'init' # 1, a, [
    text = ''
    while True:
        v = stack.pop()

        if flag == 'init':            
            if v == '[':
                assert False, v
            elif v.isnumeric():
                assert False, v
            else:
                flag = 'a'
        elif flag == 'a':
            if v == '[':
                flag = '['
            elif v.isnumeric():
                assert False, v
            else:
                flag = 'a'
        elif flag == '[':
            if v == '[':
                assert False, v
            elif v.isnumeric():
                flag = '1'
            else:
                assert False, v

        if flag == 'a':
            text = v + text
        elif flag == '1':
            text = int(v) * text
            stack.append(text)
            break






