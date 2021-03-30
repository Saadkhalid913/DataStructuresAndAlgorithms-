class Solution(object):
    def tribonacci(self, n, memo = dict()):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0 
        if n == 2 or n ==1 :
            return 1
        else:
            var = self.tribonacci(n-1) + self.tribonacci(n-3) + self.tribonacci(n-2) 
            memo[n] =var
            return var 
