# Author: Tucker Ferguson
# Date: 8/23/2020
#
# Description: Given a Binary tree return it inverted
#
# Link: https://leetcode.com/problems/invert-binary-tree/
# 
# Definition:
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        curr = root
        queue = []
        if(curr.left or curr.right):
            queue.append(curr)
            while len(queue)!= 0:
                if curr.left :
                    curr = curr.left
                    queue.append(curr)
                elif curr.right :
                    queue.append(curr)
                    curr = curr.right
                else:
                    curr = queue.pop(0)
                    print(curr.val)
                    if curr == root:
                        return curr
                    else:
                        curr.left,curr.right = curr.right,curr.left
        else:
            return None

        #currently returns exact same tree (not getting into logiclm,)