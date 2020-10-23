# Author: Tucker Ferguson
# Date: 10/12/2020
#
# Description: Given an unsorted array of integers, find the length of longest increasing
# subsequence 
#
#
# Link: https://leetcode.com/problems/longest-increasing-subsequence/
#
# Definition: 
class Solution:
    def lengthOfLIS(self,nums, total = 0):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Initialize integer variable to previous iterations value for comparison
        temp = float('-inf')
        #Integer variable to hold subsequence lengths
        maxLen = 0
        #List containing subsequence lengths
        
        
        #iterate the input sequence of integers
        if nums:
            templist = []
            for value in nums:
                if value < temp:
                    continue;
                elif value > temp:
                    temp = value
                    maxLen += 1
                    templist.append(maxLen)
            if templist:        
                tempTotal = max(templist)
            else:
                tempTotal = 1
            
            if tempTotal > total:
                total = tempTotal
            return self.lengthOfLIS(self,nums[1:],total)
        else:
            return total
#this is whats breaking it returns 2 should return 3 is definitely a last index issue
print(Solution.lengthOfLIS(Solution,[10,9,2,5,3,4]))