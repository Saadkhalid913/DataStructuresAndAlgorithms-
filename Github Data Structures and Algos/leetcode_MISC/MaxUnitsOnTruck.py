'''
    https://leetcode.com/problems/maximum-units-on-a-truck/submissions/
'''

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes = list(sorted(boxTypes, key= lambda x : x[1], reverse=True))
        total = 0 
        print(boxTypes)
        for i in range(len(boxTypes)):
            k = boxTypes[i][0]
            j = boxTypes[i][1]
            if k > 0 and truckSize > 0:
                total += min(truckSize, k) * j
                truckSize -= min(truckSize, k)
        return total 
                    
                
        
