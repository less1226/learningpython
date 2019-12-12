# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        
        fastnode = head
        slownode = head
        while fastnode != None and fastnode.next != None:
            fastnode = fastnode.next.next
            slownode = slownode.next
        
        fastnode = slownode
        while slownode.next != None:
            tempnode = slownode.next
            tempnode.next = fastnode
            fastnode, slownode = tempnode, slownode.next
            
        
        while fastnode != None:
            if fastnode.val == head.val:
                fastnode = fastnode.next
                slownode = slownode.next
            else:
                return False
            
        return True
