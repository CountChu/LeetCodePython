from typing import List
import pdb

solution_json = {
    "date": "2021/4/3",
    "coding": 25
}

class Solution:

    #
    # 2021/4/3: 25 min
    #

    def maxArea(self, height: List[int]) -> int:
        idx0 = 0                        # left
        idx1 = len(height) - 1          # right
        max_area = 0
        while True:
            num0 = height[idx0]
            num1 = height[idx1]
            min_h = num0 
            if min_h > num1:
                min_h = num1
            area = min_h * (idx1 - idx0)
            #print(idx0, idx1, min_h, area)
            if area > max_area:
                max_area = area
            
            if num0 < num1:
                idx0 += 1
            else:
                idx1 -= 1
                
            if idx0 >= idx1:
                break
                
        return max_area        
            

    #
    # 2021/4/3: 8 mins (Time Limit Exceeded)
    #

    def maxArea_v1(self, height: List[int]) -> int:
        max_a = 0
        for i in range(len(height)-1):
            for j in range(i + 1, len(height)):
                h = height[i]
                if h > height[j]:
                    h = height[j]
                a = (j - i) * h
                print(i, j, h, a)
                if max_a < a:
                    max_a = a
        return max_a
        
