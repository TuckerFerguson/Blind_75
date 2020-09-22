# Author: Tucker Ferguson
# Date: 9/21/2020
#
# Description: Given an array that is sorted in ascending order, than pivoted
# on a random index, unknown to user at runtime. 
# 
# Find the minimum value in the array, assume no duplicates
#
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums):
        #built-in for speed up
        return sorted(nums)[0]
      
