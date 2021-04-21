from typing import List
import pdb

#
# 2021/4/29: "Wrong Answer"
#

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        debug = True

        def move_right(start, stop):
            max_sum = None
            max_idx = None
            sum = 0
            for i in range(start, stop + 1):
                sum += nums[i]
                if max_sum == None:
                    max_sum = sum
                    max_idx = i
                elif max_sum < sum:
                    max_sum = sum
                    max_idx = i
            return max_idx, max_sum  

        def move_left(start, stop):
            max_sum = None
            max_idx = None
            sum = 0
            for i in range(start, stop-1, -1):
                sum += nums[i]
                if max_sum == None:
                    max_sum = sum
                    max_idx = i
                elif max_sum < sum:
                    max_sum = sum
                    max_idx = i
            return max_idx, max_sum 

        n = len(nums)
        j = n - 1
        i = 0

        #
        # Determine if move_right or move_left.
        #

        _, max_sum_right = move_right(0, j)
        if debug:
            print('j = %d, max_sum_right = %d' % (j, max_sum_right))

        _, max_sum_left = move_left(j, 0)
        if debug:
            print('i = %d, max_sum_left = %d' % (i, max_sum_left))

        move_right_first = False
        if max_sum_right > max_sum_left:
            move_right_first = True
        if debug:
            print('move_right_first = %s' % (move_right_first))

        max_sum = None


        if move_right_first:
            while True:

                j, max_sum_right = move_right(i, j)
                if debug:
                    print('j = %d, max_sum_right = %d' % (j, max_sum_right))

                i, max_sum_left = move_left(j, i)
                if debug:
                    print('i = %d, max_sum_left = %d' % (i, max_sum_left))

                if max_sum_right == max_sum_left:
                    max_sum = max_sum_right
                    break
        else:
            while True:

                i, max_sum_left = move_left(j, i)
                if debug:
                    print('i = %d, max_sum_left = %d' % (i, max_sum_left))

                j, max_sum_right = move_right(i, j)
                if debug:
                    print('j = %d, max_sum_right = %d' % (j, max_sum_right))

                if max_sum_right == max_sum_left:
                    max_sum = max_sum_right
                    break

        return max_sum