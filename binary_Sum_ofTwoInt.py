# Author: Tucker Ferguson
# Date: 7/29/2020
#
# Description: Sum of two integers without use of the addition or subtraction operator.
#
# Link: https://leetcode.com/problems/sum-of-two-integers/
# 
# Definition:
#
# class Solution(object):
#    def getSum(self, a, b):
#        :type a: int
#        :type b: int
#        :rtype: int
#        

import pdb
class solution(object):
    #Note to self: Don't overcomplicate it, use AND to find carry bit, and XOR to find addition 
    def getSum(a,b):
        binValOne = a
        binValTwo = b
    
        while binValTwo != 0 :
            carry = binValOne & binValTwo
            binValOne = binValOne ^ binValTwo
            binValTwo = carry << 1
        return binValOne

print(solution.getSum(5,5))



       


        
