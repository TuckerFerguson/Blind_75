# Author: Tucker Ferguson
# Date: 9/23/2020
#
# Description: You are given coins of different denominations, 
# and total amount of money. 
#
# Compute the fewest number of coins it takes to make up that amount.
# if not possible return -1
#
# Link: https://leetcode.com/problems/coin-change/
#
# Definition: 
class Solution:
    def helper(self,coin,runningTotal):
        return runningTotal + coin
    def coinChange(self,coins,amount):
        coinCount = 0
        valueList = []
        for coin in coins:

        
            
"""        
        while(total >= 0):
            for coin in sorted(coins)[::-1] :
                while total - coin >= 0:
                    coinCount += 1
                    total = total - coin
                    print("coin count:{} total: {}".format(coinCount,total))
            if total > 0:
                return -1
            else:
                return coinCount
"""
Solution.coinChange(Solution,[186,419,83,408],6249)     
# close this is the input breaking it
# [186,419,83,408]
#6249
# print("coin count:{} {} - {} = {}".format(coinCount,total+coin,coin,total))