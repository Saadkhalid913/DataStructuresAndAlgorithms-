'''
 https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/
'''

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        m = max(candies)
        truth = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies>=m:
                truth[i] =True 
                
        return truth 
        
