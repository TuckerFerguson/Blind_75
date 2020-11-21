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








"""
class Solution:
    def maxPathSum(self,root):
        nodeValues = {}
        queue = []
        if root == [] :
            return 0
        queue.append(root)
        while(len(queue)!=0):
            if(root.left and root.left.val not in nodeValues):
                if root.val not in nodeValues:
                    queue.append(root)
                root = root.left
            elif(root.right and root.right.val not in nodeValues):
                if root.val not in nodeValues:
                    queue.append(root)
                root = root.right
            else:
                nodeValues[root.val] = root.val
                root = queue.pop()
        for x in nodeValues.values():
            print(x)
        return max([x+x for x in nodeValues.values()])
#right now it perfectly builds tree now i must transcend it looking for the max.
"""










