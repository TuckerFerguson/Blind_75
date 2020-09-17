# Author: Tucker Ferguson
# Date: 9/16/2020
#
# Description: Design aa data structure that supports both:
# 1) void addint(num: num): <--- Add a integer number from the data stream to the data structure
# 2) double findMedian(): <--- Return the median of all elements so far
#
#
# Link: https://leetcode.com/problems/top-k-frequent-elements/
#
class MedianFinder:
    
    def __init__(self):
        self.stack = list()
        self.medianVal = 0
        
        
    def addNum(self,num:int):
        if type(num) == int:
            self.stack.append(num)
        else:
            pass
    
    def indexFinder(self):
        self.stack.sort()
        if len(self.stack)%2 == 1 :
            size = int(((len(self.stack)-1)/2))
        elif len(self.stack)%2 == 0:
            if len(self.stack) == 0:
                return 0
            else:
                start = int((len(self.stack)/2)-1)
                end = int((len(self.stack)/2))
                return[start,end]
        
        else:
            return None
        return size
            
    def findMedian(self):
        size = self.indexFinder()
        if type(size) != int and len(size) == 2:
            start = size[0]
            end = size[1]
            return (self.stack[start] + self.stack[end])/2
        elif type(size) == int:
            return self.stack[size]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()