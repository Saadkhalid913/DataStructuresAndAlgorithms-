'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        index = 0
        nodehash = {}
        temp = head 
        while head != None:
            nodehash[index] = head  
            index +=1
            head = head.next

        if ((index - n) - 1) in nodehash and (index - n + 1) in nodehash :
            nodehash[index - 1 - n].next = nodehash[index - n + 1]
        elif (index - n) in nodehash and (index - n + 1) in nodehash :
            return nodehash[index - n + 1]
        elif (index - n - 1) in nodehash and not ((index - n) + 1) in nodehash:
            nodehash[index - n -1].next = None 
            return temp 
        else:
            return None 
        return temp 
        
