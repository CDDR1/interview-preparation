# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        
        return lists[0]
        
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            
            if val1 > val2:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
                
            curr = curr.next
                
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
            
        return dummy.next
                
# Time complexity: O(n * log k)
# Space complexity: O(log k) because of the "temporary" array that is created to store the merged lists 
# Pattern: Linked Lists
# =====================================================================
# Was close to solving it on my own using the brute force approach, but
# I had to watch NeetCode's video to understand the efficient soluiton