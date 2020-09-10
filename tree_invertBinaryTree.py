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
        queue = []
        self.root = root
     #case 0) is root ?   y: cont   n: return []
        if(root is []):
            return []
        else:
            queue.append(root)
            while len(queue) != 0:
     #case 4) there is a left and right
                root = queue.pop(0)
                root.left,root.right = root.right,root.left
                if root.left:
                    queue.append(root)                    
                if root.right:
                    queue.append(root.right)
            return root
          

        
                    
     
   


            

     