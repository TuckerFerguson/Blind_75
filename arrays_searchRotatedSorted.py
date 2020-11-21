# Author: Tucker Ferguson
# Date: 11/2/2020
#
# Description:You are given an integer array nums sorted in ascending order, and an integer target.
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# If target is found in the array return its index, otherwise, return -1.
# 
#
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in sorted(nums):
            return nums.index(target)
        else:
            return -1
print(Solution.search(Solution,range(10),4))