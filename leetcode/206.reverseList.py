# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        if head.next == None:
            return head
        
        tempnode = head.next
        head.next = None
        while tempnode.next:
            lnode = tempnode
            tempnode = tempnode.next
            lnode.next = head
            head = lnode
        
        tempnode.next = head
        return tempnode
            
            
