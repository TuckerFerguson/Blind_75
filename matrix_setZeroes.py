# Author: Tucker Ferguson
# Date: 8/31/2020
#
# Description: Given an m x n matrix. If an element is 0, set its entire row and column to 0. 
# Do it in-place.
#
# Link: https://leetcode.com/problems/set-matrix-zeroes/
# 
# Definition:
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        #each list element of the list container
        for x in matrix:
            #iterate each emmeber of child list element
            for i in range(len(x)):
                if x[i] == 0 :
                    #to do change row and col to 0
                
                
            
print(Solution.setZeroes(Solution,[]))