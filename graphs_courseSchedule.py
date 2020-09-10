# Author: Tucker Ferguson
# Date: 9/4/2020
#
# Description: Given 'n' courses you have to attend from 0 to n-1 
# Some courses have prerequisites, expressed as a pair etc: [0,1] (0 is prereq to 1)
# Can you finish all courses given n, and a list of prereqs
# 
#
# https://leetcode.com/problems/course-schedule/
#
# Definition:
#
# class Node(object):
#    def __init__(self, val = 0, neighbors = None):
#        self.val = val
#        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #creates a dict out of the prequisites 
        reqDict = {}
        
        for req in prerequisites:
            
            #TO DO I want a key with list value of all preqs that involve it 
            reqDict[req[0]].update(req[1])
        
        
        
        return reqDict
        
        
        
        #This is the range from 0 to n-1
        for x in range(numCourses-1):
            node = Node(x)
            
        
print(Solution.canFinish(Solution,6,[[0,1],[1,2],[0,2]]))