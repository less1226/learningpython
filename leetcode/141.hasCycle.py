# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fastnode = head
        while True:
            if fastnode == None or fastnode.next == None:
                return False
            else:
                fastnode = fastnode.next.next
                if fastnode == head:
                    return True
                head = head.next