# Author: Tucker Ferguson
# Date: 8/9/2020
#
# Description: Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
#
# Link: https://leetcode.com/problems/clone-graph/
#
# Definition:
# 
# class Node(object):
#    def __init__(self, val = 0, neighbors = None):
#        self.val = val
#        self.neighbors = neighbors if neighbors is not None else []
#
class Solution(object):
    #dfs solution
    nodeDict = {}
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return [[]]
        if node in self.nodeDict:
            return nodeDict[node]
        nodeCopy = Node(n.val)
        self.nodeDict[n] = nodeCopy
        #create a neighbors attribute of nodeCopy object
        nodeCopy.neighbors = []
        for val in node.neighbors:
            nodeCopy.neighbors.append(cloneGraph(val))
        return nodeCopy

        #next lets do a BFS solution on our own!! cash money

            





