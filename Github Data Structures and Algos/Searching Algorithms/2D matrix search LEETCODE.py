'''
https://leetcode.com/problems/search-a-2d-matrix/submissions/
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        i = 0
        j = 0
        while True:
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] < target:
                i +=1 
            elif matrix[i][0] > target:
                i -=1 
                break 
            if i == len(matrix):
                i-=1 
                break 
        while j < len(matrix[0]):
            if matrix[i][j] == target:
                return True 
            elif matrix[i][j] < target:
                j +=1
            elif matrix[i][j] > target:
                return False 
        return False 
            
            
        
