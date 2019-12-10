# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        head = ListNode(0)
        dummynode = ListNode(0)
        dummynode.next= head
        
        if l1.val <= l2.val:
            head.val = l1.val
            l1 = l1.next
        else:
            head.val = l2.val
            l2 = l2.next
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next
        
        if l1 == None:
            head.next = l2
        else:
            head.next = l1
        
        return dummynode.next
            
