"""
Author: Tucker Ferguson
Date: 7/27/2020

Description: Reverse a Linked List, both iteratively and recursively 

https://leetcode.com/problems/reverse-linked-list/

class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverse(self,head):
        type head: ListNode
        type return: LinkedNode
"""
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
    
    
class Solution(object):
    def reverse(self,head): 
        curr = ListNode(head.val)
        prev = None
        while curr.next is not None :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head
print(Solution())    











