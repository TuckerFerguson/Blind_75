# Author: Tucker Ferguson
# Date: 8/23/2020
#
# Description: Given a linked list determine if any cycles
# exist in it
#
# Link: https://leetcode.com/problems/linked-list-cycle/
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        values = []
        #iterate through linked list node by node
        while curr.next:
            curr = curr.next
            #Check for node.val in values list, if true repeat/cycle return True
            if curr.val in values :
                return True
            else: 
                values.append(curr.val)
        return False
