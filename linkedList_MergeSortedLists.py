# Author: Tucker Ferguson
# Date: 9/3/2020
#
# Description: Merge two sorted linked lists and return it as one sorted list
#
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# 
# Definition: 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.sortedList = []
        curr = l1
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        while curr or l2 :
            if curr.val <= l2.val :
                if(curr.val < l2.val):
                    self.sortedList.append(curr.val)
                    curr = curr.next
                elif(curr.val == l2.val):
                    self.sortedList.append(curr.val)
                    curr = curr.next
                    self.sortedList.append(l2.val)
                    l2 = l2.next
            else :
                while(l2.val < curr.val):
                    self.sortedList.append(l2.val)
                    l2 = l2.next
        if(self.sortedList ):
            head = ListNode(self.sortedList[0])
            curr = head
            for x in self.sortedList[1:]:
                curr.next = ListNode(x)
                curr = curr.next
            return head
        else:
            return None