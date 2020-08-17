"""
Author: Tucker Ferguson
Date: 8/14/2020

Description: Given a collection of intervals, merge all overlapping intervals

Link: https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
"""
class Solution(object):
    def mergeIntervals(self,intervals):
        self.intervList = intervals
        mergedIntervals = []
        for i,interv in enumerate(intervals):
            
            if(i >= 1):
                prev = self.intervList[i-1]
                current = interv

                if(prev[1] >= current[0]):
                    mergedIntervals.append([prev[0],current[1]])
                else:
                    mergedIntervals.append(current)
        return mergedIntervals
        #print("in: {}\n out: {}".format(self.intervList, mergedIntervals))
        #[x for x in ]
Solution.mergeIntervals(Solution,[[1,3],[2,6],[8,10]])