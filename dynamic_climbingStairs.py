# Author: Tucker Ferguson
# Date: 9/9/2020
#
# Description: You are climbing a staircase, it takes n steps to reach the top.
# You can take either 1 or 2 steps each attempt to climb. How many distinct ways is there to reach the top
#
# Link: https://leetcode.com/problems/climbing-stairs/
# 
# Definition:
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #dict to hold total number of steps throughout iteration setDict['n'] = setDict[(n-1)] + setDict[(n-2)]
        setDict = {}
       
        for num in range(4):
            setDict[num] = num
        for stair in range(4, n+1):
            setDict[stair] = setDict[stair-1] + setDict[stair-2]
            
        return setDict[n]
     