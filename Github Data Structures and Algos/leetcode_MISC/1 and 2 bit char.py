'''
https://leetcode.com/problems/1-bit-and-2-bit-characters/submissions/
'''

class Solution(object):
  
  
    def isOneBitCharacter(self, bits):
        i=0
        while i < len(bits) -1: # loop through the entire list 
            i += bits[i] +1 # if bits[i] == 1, we can skip the next char, increment i by 2 (bits[i] + 1) if bits[i] is 0, we move over one char
            # if at the end, we are at the end of the array, it means that the last character is a one bit character, otherwise, we have skipped over
            # the last char, meaning that the last char was a two bit character
            return i == len(bits) - 1
