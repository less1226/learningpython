# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True

        fastnode = head
        slownode = head
        while fastnode != None and fastnode.next != None:
            fastnode = fastnode.next.next
            slownode = slownode.next

        fastnode = None
        while slownode != None:
            tempnode = slownode.next
            slownode.next = fastnode
            fastnode = slownode
            slownode = tempnode

        while fastnode != None:
            if fastnode.val == head.val:
                fastnode = fastnode.next
                head = head.next
            else:
                return False

        return True