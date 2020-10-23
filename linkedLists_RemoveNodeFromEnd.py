# Author: Tucker Ferguson
#
# Date: 10/23/2020
#
# Description: Given the head of a linked list, remove the n'th
# node from the end of the list and return its head
#
#   
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        queue = []

        while(curr):
            queue.append(curr)
            curr = curr.next
            
        curr = queue[::-1].pop(n)
        print(curr.val)
        prev = curr
        curr = curr.next
        prev.next = curr.next

        return head

Solution.removeNthFromEnd(Solution, [1,2,3,4,5],2)