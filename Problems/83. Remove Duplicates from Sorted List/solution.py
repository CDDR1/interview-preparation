# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        l = None
        r = head
        seen = set()
        
        while r:
            if r.val in seen:
                l.next = l.next.next
                r = l.next
            else:
                seen.add(r.val)
                l = r
                r = r.next
                
        return head
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Linked List
# Time used: 8min