from typing import List
import pdb

#
# 2021/5/21: 18, 16, Time Limit Exceeded
#

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    	d = False
    	v = temperatures
    	n = len(v)
    	q = []  # q = [(temp, days)]

    	ctx = {'out': []}
    	for i in range(n):
    		append(q, v[i])
    		consume(q, ctx)

    		if d:
    			print(q)

    	out = ctx['out']
    	for temp, days in q:
    		out.append(days)
    	return out

def append(q, temp):
	q.append([temp, 0])
	last_temp = q[-1][0]	
	for i in range(len(q) - 1):
		temp, days = q[i]
		if days == 0 and temp < last_temp:
			q[i] = [temp, len(q) - 1 - i]

def consume(q, ctx):
	if len(q) <= 1:
		return

	while True:
		if q[0][1] == 0:
			break
		else:
			temp, days = q.pop(0)
			ctx['out'].append(days)