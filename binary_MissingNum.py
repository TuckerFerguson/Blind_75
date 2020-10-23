# Author: Tucker Ferguson
# Date: 10/16/2020
#
# Description: Given an array nums containing n distinct 
# numbers in the range [0, n], return the only number in 
# the range that is missing from the array.
#
# Bonus: Implement with O(1) space complexity and O(n) runtime complexity
#
# https://leetcode.com/problems/missing-number/
# 
# 
#
# Definition:
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i,num in enumerate(sorted(nums)):
            if i != num:
                return i
        return len(nums)
print(Solution.missingNumber(Solution,[0,1]))       

        

