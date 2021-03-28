'''

https://leetcode.com/problems/maximum-subarray/

'''



class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        m = nums[0]
        h = {0:nums[0]}
        for i in range(1, len(nums)):
            h[i] = max(nums[i], nums[i] + h[i-1])
            if h[i] > m:
                m = h[i]
        return m 
            
            
