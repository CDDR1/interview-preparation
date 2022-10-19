# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum = None
        l = l1
        r = l2
        curr = None
        valLeft = None
        
        while (l != None) and (r != None):
            valSum = l.val + r.val
            if valLeft != None:
                valSum += valLeft
                valLeft = None
                
            if valSum > 9:
                strSum = str(valSum)
                newNode = ListNode(int(strSum[1]))
                valLeft = int(strSum[0])
            else:
                newNode = ListNode(valSum)
                
            if sum == None:
                sum = newNode
                curr = sum
            else:
                curr.next = newNode
                curr = curr.next
                
            l = l.next
            r = r.next
            
        
        if l == None:
            while r != None:
                valSum = r.val
                if valLeft != None:
                    valSum += valLeft
                    valLeft = None
                if valSum > 9:
                    strVal = str(valSum)
                    newNode = ListNode(int(strVal[1]))
                    valLeft = int(strVal[0])
                else:
                    newNode = ListNode(valSum)
                curr.next = newNode
                curr = curr.next
                r = r.next
        elif r == None:
            while l != None:
                valSum = l.val
                if valLeft != None:
                    valSum += valLeft
                    valLeft = None
                if valSum > 9:
                    strVal = str(valSum)
                    newNode = ListNode(int(strVal[1]))
                    valLeft = int(strVal[0])
                else:
                    newNode = ListNode(valSum)
                curr.next = newNode
                curr = curr.next
                l = l.next
                
        if valLeft != None:
            curr.next = ListNode(valLeft)
            
        return sum
    
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Linked Lists
# Time used: 51 min
                    
                    
                    
                    
                    