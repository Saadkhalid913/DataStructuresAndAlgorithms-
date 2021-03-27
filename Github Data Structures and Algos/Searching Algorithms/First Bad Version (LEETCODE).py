'''

https://leetcode.com/problems/first-bad-version/submissions/

'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        i = 0
        j = n
        
        while (j - i) > 1:
            m = (i + j) // 2
            if isBadVersion(m):
                j = m
            else:
                i = m
            
        return j 
            
