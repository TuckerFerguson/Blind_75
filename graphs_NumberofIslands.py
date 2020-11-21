# Author: Tucker Ferguson
# Date: 10/30/2020
#
# Description: Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
#
# Link: https://leetcode.com/problems/number-of-islands/
#
# Definition:
# 
# class Node(object):
#    def __init__(self, val = 0, neighbors = None):
#        self.val = val
#        self.neighbors = neighbors if neighbors is not None else []
#
class Solution(object):
    

    def numIslands(self, grid):

        """
        :type grid: List[List[str]]
        :rtype: int
        """
        graph = {}
        outgraph = {'corner':[],
                    'left':[],
                    'right':[],
                    'top':[],
                    'bottom':[],
                    'middle':[]
                    }
            
        island = 0
        length = len(grid[0])
        height = len(grid)

        for i in range(length*height) :
            neighbors = []

            if (i  % length == 0): 
                graph[i] = "left"
            elif(i % length == length-1):
                graph[i] = "right"
        
            elif(i < length):
                graph[i] = "top"
            elif(i > (length*height)-(length)):
                graph[i] = "bottom"
            else:
                graph[i] = 'middle'
           

        for i in range(length * height):
            if graph[i] == 'left':
                outgraph['left'].append(i)
            elif graph[i] == 'right':
                outgraph['right'].append(i)
            elif graph[i] == 'top':
                outgraph['top'].append(i)
            elif graph[i] == 'bottom':
                outgraph['bottom'].append(i)
            elif graph[i] == 'corner':
                outgraph['corner'].append(i)
            else: 
                outgraph['middle'].append(i)
    
        outgraph['corner'] = [outgraph['left'][0],outgraph['left'][height-1],outgraph['right'][0],outgraph['right'][height-1]]
        for v in outgraph['corner']:
            if v in outgraph['left']:
                outgraph['left'].remove(v)
            elif v in outgraph['right']:
                outgraph['right'].remove(v)

        
        return outgraph
       
            
        #to do break apart the graph now that we have dimensions of each vertex and edge, check for neighbors == 1

print(Solution.numIslands(Solution,
[["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]))
        
            

        
        
        
        
        
        
        
        
        
        
        