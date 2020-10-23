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
        keyVal = 0
        coordDict = {}
        #each list element of the list container
        for j,item in enumerate(matrix):
            for i in range(len(item)):
                coord = [j,i]
                coordDict[keyVal] = [item[i],coord]
                keyVal = keyVal + 1
            #iterate each emmeber of child list element
            #for i in range(len(x)):
                #if x[i] == 0 :
                    #to do change row and col to 0
        for index in range(len(coordDict.values())):
            if coordDict[index][0] == 0:
               index = coordDict[index][1][0]
               zero_Index = coordDict[index][1][1]
               matrix[index] = [x*0 for x in range(len(matrix[0]))]
               for val in matrix:
                   val[zero_Index] = 0

               continue;
              
        return matrix
print(Solution.setZeroes(Solution,[[1,1,1],[1,0,1],[1,1,1]]))