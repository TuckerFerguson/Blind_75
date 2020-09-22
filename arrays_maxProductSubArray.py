# Author: Tucker Ferguson
# Date: 9/18/2020
#
# Description: Given an array of integers, locate a subarray that is a child of the input
# (must contain atleast one number) with the largest product
#
# Link: https://leetcode.com/problems/maximum-product-subarray/
#

class Solution:
    def maxProduct(self, nums):
        productDict = {}
        nums = [2,3,-2,4]
        
        for i,num in enumerate(nums):
            productDict[num] = num
            productval = nums[i]
            for j in range(i,(len(nums)-1)):
                productval = productval * nums[j+1]
                productDict[productval] = productval
        return max([x for x in productDict.values()])     
        print(productDict)
print(Solution.maxProduct(Solution,[1,1]))
# to do
# current out put {2: -8, 0: -48, 1: -24} so contains some of the right answers.
#

