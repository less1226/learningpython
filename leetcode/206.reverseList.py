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

        cur = None
        while head:
            temphead = head.next
            head.next = cur
            cur, head = head, temphead

        return cur
