# Author: Tucker Ferguson
# Date: 8/2/2020
#
# Description: Given a binary tree, find the max depth of its child nodes 
#
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 
# Definition:
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #L <--- Origin -----> R
        #psuedo first check L nodes tree's depth, next check R nodes tree depth as well compare
        #largest in value is the max depth
        
        #Variables
        leftDepth = 0
        rightDepth = 0
        self.root = root
        depth = 0

        #Check for any children of root if so we assign each child to its correlated position
        if root.left or root.right is True:
            leftChild = root.left
            rightChild = root.right
            #set max depth counter, and its iterating sum depth.
            depth = 1
            maxDepth = 0
            #1) first we start on left side of tree and collect its max depth. 
            parent = leftChild
            while(parent.left or parent.right):
                if(parent.left):
                    depth += 1
                    parent = parent.left
                elif(parent.right):
                    depth += 1
                    parent = parent.right
                else:
                    if(depth > maxDepth):
                        maxDepth = depth
                        depth = 1
                        #2) Repeat process for right side
                        parent = rightChild
                    #LOGIC HERE IF DEPTH(ITERATING SUM) IS LARGER THAN STORED VALUE FOR MAXDEPTH, then we set maxdepth to this new value reset the 
                    #iterative sum then move to the right side of the tree.

                    #now on second iteration on right side of tree we check to see if at the end the iterative depth is larger than maxDepth if so maxdepth is set to this new depth, 
                    #and the process is repeated, however now the else conditional will be entered, which returns the maxDepth
                    else:   
                        return maxDepth
                
        else:
            return 0
Solution()