# Tucker Ferguson
# 11/21/2020

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.
# top 94% of leetcode users cause this beatiful library and its dequeue method below
from collections import deque
class llist:
    def __init__(self):
        head = None;
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        queue = deque()
        queueOutput = deque()
        node = head
        if head is None:
            return head
        if head.next is None:
            return head
        while node:
            queue.append(node)
            node = node.next
        while len(queue) != 0:
            if(len(queue) == 1):
                queueOutput.append(queue.pop())
            else:
                queueOutput.append(queue.popleft())
                queueOutput.append(queue.pop())
        
        head = queueOutput.popleft()
        node = queueOutput.popleft()
        head.next = node
        while(len(queueOutput) != 0):
            node.next = queueOutput.popleft()
            node = node.next    
        node.next = None
        

#instantiate list
llist = llist()

#populate first element of llist (node) and assign it as head
node1 = ListNode(1)
llist.head = node1

#fill list with nodes (2-5)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(3)
node2.next = node3
node4 = ListNode(4)
node3.next = node4
#node5 = ListNode(5)
#node4.next = node5
#node5.next = None

print(Solution.reorderList(Solution,llist.head))
"""
        (Pdb) print([x.val for x in queue]) 
        [1, 3, 5]
        (Pdb) print([x.val for x in queue2]) 
        [2, 4]
"""

