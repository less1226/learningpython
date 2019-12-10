# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummynode = ListNode(0)
        dummynode.next = head
        firstnode = dummynode
        secondnode = dummynode
        i = 0
        while i < n:
            firstnode = firstnode.next
            i+=1
        
        while firstnode.next:
            firstnode = firstnode.next
            secondnode = secondnode.next
        
        secondnode.next = secondnode.next.next
        
        return dummynode.next
