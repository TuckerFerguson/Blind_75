# Author: Tucker Ferguson
# Date: 8/12/2020
#
# Description: 
# 
# - Given an array for which the ith element is the price of a 
# a given stock on on day i
#
# - Design an algorithm to find the maximum profit possibile with a
# single transaction limit, note selling prior to buying is not allowed 
# 
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# 
class Solution(object):
    def maxProfit(self,prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.priceList = prices
        
