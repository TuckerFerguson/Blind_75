# Author: Tucker Ferguson
# Date: 8/19/2020
#
# Description: Given an unsigned integer, return the number of 
#              1 bits it has (Hamming weight)
#
# Link: https://leetcode.com/problems/number-of-1-bits/
# 
# Definition:
#
# class Solution(object):
#    def hammingWeight(self, n):
#        """
#        :type n: int
#        :rtype: int
#        """
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binInt = bin(n)
        onesCount = 0
        for bit in binInt[2:] :
            if int(bit) == 1:
                onesCount += 1
        return onesCount
       
S = Solution.hammingWeight(Solution,11)
print("input: 11 or Binary: 0000000000001011, output: {}".format(S))