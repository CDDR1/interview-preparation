# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        l = None
        r = head
        
        while r:
            if l and r.val == l.val:
                l.next = l.next.next
                r = l.next
            else:
                l = r
                r = r.next
                
        return head
    
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Linked List