from typing import List
import pdb

solution_json = {
    "date": "2021/5/22",    
    "design": 6,
    "coding": 13,
    "runtime": "72 ms",
    "memory": "14.7 MB"
}    

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    	d = False
    	v = tokens
    	n = len(v)
    	stack = []
    	for i in range(n):
    		if v[i] in ['+', '-', '*', '/']:
    			v1 = stack.pop()
    			v0 = stack.pop()
    			if v[i] == '+':
    				v2 = int(v0) + int(v1)
    			elif v[i] == '-':
    				v2 = int(v0) - int(v1)
    			elif v[i] == '*':
    				v2 = int(v0) * int(v1)
    			elif v[i] == '/':
    				#pdb.set_trace()
    				v2 = int(int(v0) / int(v1))
    			else:
    				assert False
    			stack.append(str(v2))		
    		else:
    			stack.append(v[i])

    		if d:
    			print(stack)

    	out = stack.pop()
    	out = int(out)
    	return out