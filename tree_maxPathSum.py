# Author: Tucker Ferguson
# Date: 9/13/2020
#
# Description: Given a binary tree, find the maximum path sum. 
# The input will not be empty.
#
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self,root):
        self.weight = 0
        d = {}
        queue = []
        seen = []
        if root.val < 0 :
            curr = root
            curr.val = 0
            queue.append(curr)
        else:
            curr = root
            queue.append(curr)
        self.weight += curr.val
        while(len(queue)!=0):
            if curr.left or curr.right: 
                if curr not in seen:
                    queue.append(curr)
                    self.weight += curr.left.val 
                    self.weight += curr.right.val
                if curr.left:
                    curr = curr.left
                elif curr.right:
                    curr = curr.right
            else:
                d[curr.val] = self.weight
                curr = queue.pop(0)
                seen.append(curr)
        l = [x for x in d.values()]
        print(d)
        return max(l)

#right now works for base case and is semi working for more difficult cases , it needs to handle recursion

