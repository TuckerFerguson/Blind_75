# Author: Tucker Ferguson
# Date: 9/28/2020
#
# Description: Given a (m x n) matrix of non-negative integers 
# each integer represents the height of each unit cell in a continent
# 
# Pacific touches: left and top edges
# Atlantic touches: right and bottom edges
# Water can flow in four directions (up, down, left, right) from one cell to another
# one with a height equal or lower
# 
# Find and list the coordinates that allow water to flow from Pacific to Atlantic, vice versa
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/
#
# Definition:
#
# class Solution:
#    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

# Create Dictionary that contains reference to all neighbors of a current cell

matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
#answer ---> [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] 
myDict = {}

#generic key value for indexing our dictionary later
index = 0

#coordinate list
coordList = []

# matrix(m x n)
m = len(matrix[0])
n = len(matrix)

for i in range(m):
    
    for j in range(n):
        #print("i:{}, j:{}".format(i,j))
        #myDict[matrix[i][j]] = [matrix[i-1][j], matrix[i][j-1], matrix[i+1][j], matrix[i][j+1]]
        myDict["Cell {}-->".format(index)] = matrix[i][j]
        index = index + 1
print(myDict)
