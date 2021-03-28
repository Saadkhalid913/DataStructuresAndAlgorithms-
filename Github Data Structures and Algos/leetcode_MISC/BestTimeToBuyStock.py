'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
'''
class Solution(object):
    def maxProfit(self, prices):
        mp = float("inf")
        mxp = 0
        for i in range(len(prices)):
            if prices[i] < mp:
                mp = prices[i]
            elif (prices[i] - mp > mxp):
                mxp = prices[i] - mp
            
        return mxp
        
