# Author: Tucker Ferguson
# Date: 8/26/2020
#
# Description: Given a non-negative integer, for the range (0 to input num) calc the number of 1's,
# in each number. return an array of how many 1's appear in each number of the range
#
# https://leetcode.com/problems/counting-bits/
# 
# Definition:
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #return array
        self.oneCount = []

        #values in (0 <= value <= num)
        for i in range(0,num+1):
            #get 1's count in each values binary representation
            count = bin(i).count('1')
            #append the values to return array
            self.oneCount.append(count)
        return self.oneCount
        

