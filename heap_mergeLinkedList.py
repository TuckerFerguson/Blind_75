# Author: Tucker Ferguson
# Date: 8/3/2020
#
# Description: Merge k sorted linked lists and return it as one sorted lists
# Also describe its complexity
#
# Link: https://leetcode.com/problems/merge-k-sorted-lists/
#
# class Solution(object):
#    def mergeKLists(self, lists):
#        """
#        :type lists: List[ListNode]
#        :rtype: ListNode
#        """
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return
class Solution(object):
    def mergeKList(self,lists):
        #merge the lists as per directions
        mergedLists = list()
        self.lists = lists
        for l in lists:
            while(l) :
                mem = l.val
                mergedLists.append(mem)
                l = l.next
        mergedLists.sort()
        head = pointer = ListNode(0)
        for val in mergedLists:
           node = ListNode(val)
           pointer.next = node
           pointer = node 
        return head.next

        
s = Solution()
print(s.mergeKList([[1,4,5],[1,3,4],[2,6]]))

"""Solution: class Solution(object):
    def mergeKLists(self,lists):
        mergedLists = list()
        for l in lists:
            while(l) :
                mem = l.val
                mergedLists.append(mem)
                l = l.next
        mergedLists.sort()
        head = pointer = ListNode(0)
        for val in mergedLists:
            node = ListNode(val)
            pointer.next = node
            pointer = node 
        return head.next
"""        