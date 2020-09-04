# Author: Tucker Ferguson
# Date: 8/27/2020
#
# Description: Given a string, find the length longest substring without
# repeating characters
#
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 
# Definition:


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        tempLen = 0
        cL = [x for x in s]
        temp = {}
        for c in cL:
            if(c in temp):
                temp = {}
                temp[c] = c
                tempLen = 1
            elif(c not in temp):
                temp[c] = c
                tempLen += 1
                if(tempLen > maxLen):
                    maxLen = tempLen
        return maxLen
