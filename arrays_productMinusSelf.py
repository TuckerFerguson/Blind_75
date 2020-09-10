# Author: Tucker Ferguson
# Date: 9/7/2020
#
# Description: Given an array of integers num in which n > 1. return array 'output' such that
# output[i] is equal to the product of all the elements of input array, except nums[i]
#
# Link: https://leetcode.com/problems/product-of-array-except-self/
# 
# Definition:
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for x in nums:
            l = [y for y in nums if y != x ]
            temp = 1
            for val in l :
                temp = val * temp
            output.append(temp)
        return output
    
    