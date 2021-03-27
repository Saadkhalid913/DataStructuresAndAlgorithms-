'''
https://leetcode.com/problems/set-matrix-zeroes/submissions/

'''
class Solution(object):
    def setZeroes(self, matrix):
        '''
            time complexity O(n^2)
            space complexity O(1)
        '''

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None
                    for l in range(m):
                        if matrix[l][j] != 0:
                            matrix[l][j] = None

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        return matrix



