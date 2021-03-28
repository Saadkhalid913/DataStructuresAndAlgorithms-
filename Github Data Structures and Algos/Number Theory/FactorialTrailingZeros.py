'''
   https://leetcode.com/problems/factorial-trailing-zeroes/submissions/
'''

class Solution(object):
    def trailingZeroes(self, n):
        zeros = 0
        for i in range(1, n + 1):
            p = 1
            while True:
                
                if i % (5**p) == 0:
                    zeros +=1 
                    p +=1
                else:
                    break 
        return zeros 
