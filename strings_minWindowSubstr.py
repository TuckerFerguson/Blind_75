# Author: Tucker Ferguson
# Date: 10/18/2020
#
# Description: Given a string S and a string T, find the minimum window in S 
# that contains all the characters in T. in O(n)
# - if no window in S covers all of T, return ""
# - window is guaranteed to be unique to string, if existant
#
# Link: https://leetcode.com/problems/minimum-window-substring/
#
# Definition:
import re
class Solution:
    def minWindow(self,s,t,):
        """
        :type s: str
        :type t: str
        """
        temp = ""
        index = 0
        subStrDict = {}
        for i,char in enumerate(s):
            temp += char
            subStrDict[i] = temp
        index = len(s)-1
        for j in range(len(s)):
            subStrDict[index] = s[j:]
            index += 1
        for val in subStrDict.values():
            print(val)
        
print(Solution.minWindow(Solution,"ADOBECODEBANC","ABC"))

#populating dict with every possible substring, now u must search each one for the correct substr characters ^t[0] ... t[end]$