# Author: Tucker Ferguson
# Date: 8/21/2020
#
# Description: Given a non-empty array of integers, return
# the k most frequent elements
#
# Link: https://leetcode.com/problems/top-k-frequent-elements/
#
# class Solution(object):
#    def topKFrequent(self, nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: List[int]
#     """
class solution(object):
    def topKFrequent(self,nums,k):
        #convert to set to remove duplicate entries
        keys = set(nums)
        countList = []
        for num in keys:
            countList.append((num,nums.count(num)))
            countList.sort()
        #Pretty pythony, list comprehension, tuple indexing and slicing 
        return[x[0] for x in countList[:k]]
        
print(solution.topKFrequent(solution,[1,1,1,2,2,3],2))
