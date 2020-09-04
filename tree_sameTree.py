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
        #recursive way
        def isSameTree(self, p, q):
            if not p and not q :
                return True
            if not q or not p :
                return False
            if p.val != q.val:
                return False
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            
            
            
                   
            
               
            
            
        #2) use same method on both TreeNodes

        #3) compare each node as you index into tree, compare

        #4) on unequality terminate, return false
        #5) if both trees indexed entirely return true