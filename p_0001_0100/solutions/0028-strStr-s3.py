from typing import List
import pdb

solution_json = {
    "date": "2021/4/23",
    "coding": 8,
    "runtime": "52 ms",
    "memory": "15.9 MB"
}    

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    	d = False
    	s = haystack
    	t = needle

    	if t == '':
    		return 0

    	m = len(s)
    	n = len(t)

    	j = 0
    	idx = -1
    	for i in range(m):
    		if d:
    			print(i, s[i])
    		
    		while True:
    			if j == n:
    				idx = i
    				break

    			if i + j >= m:
    				break

    			if s[i+j] == t[j]:
    				j += 1
    			else:
    				j = 0
    				break

    		if idx != -1:
    			break

    	#pdb.set_trace()
    	return idx