# Author: Tucker Ferguson
# Date: 8/16/2020
#
# Description: Given two binary trees, create a function to determine
# if they are the same
#
# Link: https://leetcode.com/problems/same-tree/
# 
# Definition:
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """