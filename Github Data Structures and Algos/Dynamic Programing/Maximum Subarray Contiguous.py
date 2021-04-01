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
            # we loop through the array and store the longest subarray which ends at element i-1 (inclusive)
            # adding the element at index i to the maximum sum at index i - 1 would result in a higher sum than simply 
            # starting a new array with length 1 (only including one element, arr[i]), then we update the dictionary 
            # to account for the inclusion of the element at index i.
            # if the element at index[i] + the value of the max subarray at i-1 is not higher than 
            # the value of arr[i], we simply start a new array at arr[i], becuase that new array would, by definition, 
            # be of a greater value than whatever array ended at index i-1.
            
            
            # example:
            # arr [1,4,-6,8,1]
            
            
            # h   [1,5,-1,8,9]
            #notice how at index 0,1 and 2, we add element i to the previous sum,
            # but at index 3, we do not add the element to the previous indexed sum, we 
            # simply set the max array value to the value of the element. becuase max(8, 8 + (-1)) = 8.
            #and for index 4, we also add the item at i to the previous sum
            
            h[i] = max(nums[i], nums[i] + h[i-1])
            if h[i] > m: # we see if the max sum at index i is higher than the currently recorded max sum
                         # if True, we update the max sum.
                m = h[i]
        # we return the max sum (int)
        return m 
            
            
