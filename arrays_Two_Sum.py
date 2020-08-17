# Author: Tucker Ferguson
# Date: 8/8/2020
#
# Description: Given an array of integers, return the indices of the two 
# numbers such that their sum is equal to a specified target value
#
# Link: https://leetcode.com/problems/two-sum/
#
class Solution:
    def twoSum(self, arry, targ):
        self.numList = arry
        #iterate through array 1 element at a time
        for value in (self.numList) :
            for x in arry:
                if(x != value and value + x == targ ):
                    #print("{},{}".format(value,x))
                    #print("{},{}".format(self.numList.index(value),arry.index(x)))
                    return([self.numList.index(value),arry.index(x)])

       
