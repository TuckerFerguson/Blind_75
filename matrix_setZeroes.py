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
        zeroIndex = []
        for i, coord in enumerate(matrix):
            for val in coord:
                if val == 0:
                    zeroIndex.append([i, coord.index(val)])
        if len(zeroIndex) > 0:
            while len(zeroIndex) >= 1:
                rowCol=zeroIndex.pop()
                zeros = []
                for x in range(len(matrix[0])):
                    zeros.append(0)
                matrix[rowCol[0]][::] = zeros
                
                for i in range(len(matrix)):
                    matrix[i][rowCol[1]] = 0
                
        














        # """
        # :type matrix: List[List[int]]
        # :rtype: None Do not return anything, modify matrix in-place instead.
        # """
        # keyVal = 0
        # coordDict = {}
        # #each list element of the list container
        # for j, item in enumerate(matrix):
        #     for i in range(len(item)):
        #         coord = [j, i]
        #         coordDict[keyVal] = [item[i], coord]
        #         keyVal = keyVal + 1
        #     #iterate each emmeber of child list element
        #     #for i in range(len(x)):
        #         #if x[i] == 0 :
        #         #to do change row and col to 0
        # for index in range(len(coordDict.values())):
        #     if coordDict[index][0] == 0:
        #        index = coordDict[index][1][0]
        #        zero_Index = coordDict[index][1][1]
        #        matrix[index] = [x*0 for x in range(len(matrix[0]))]
        #        for val in matrix:
        #            val[zero_Index] = 0

        #        continue

        # return matrix
print(Solution.setZeroes(Solution, [[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
