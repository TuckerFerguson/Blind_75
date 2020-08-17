"""
Author: Tucker Ferguson
Date: 7/26/2020

Description: Given a set of non-overlapping intervals, insert a new set interval into the intervals (merge if necessary)

Link: https://leetcode.com/problems/insert-interval/

insert(self,intervals,newInterval):
    type intervals: List[List[int]]
    type newInterval: List[int]
    rtype: List[List[int]]
"""

class Solution(object):
    def insert(self,intervals,newInterval):
        newList = []
        listCutter = []
        listSize = 2
        for i in range(2):
            for x in range(intervals[int(i)][0],(intervals[int(i)][1])+1):
                newList.append(x)
        for value,i in enumerate(newList) :
            if(value < newInterval[0]):
                newList.insert(i+1,newInterval[0])
                newList.insert(i+2,newInterval[1])
                break
        listCutter = [newList[i:i+listSize] for i in range(0,len(newList),listSize)]
        return(listCutter)

s = Solution()
print(s.insert([[1,2],[5,6]],[3,4]))


