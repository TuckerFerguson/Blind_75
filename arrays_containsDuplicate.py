# Author: Tucker Ferguson
# Date: 9/2/2020
#
# Description: Given an array of integers, find if the array contains
# any duplicate values, 
#
# Link: https://leetcode.com/problems/contains-duplicate/
# 
# Definition:
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #leveraging the fact that P3 set container eliminates duplicates
        check = set(nums)
        if len(nums) == len(check):
            return False
        else:
            return True