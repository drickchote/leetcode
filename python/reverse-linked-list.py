# Leetcode - #206 - Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Solution

# -> time:  O(n)
# -> space: O(1)

# Idea:
# input: 1 -> 2 -> 3 -> 4 -> 5
# 1 -> do nothing
# 2 -> save 3 and point to 1 
# 3 -> save 4 and point to 2
# 4 -> save 5 and point to 4
# 5 -> save None and point to 4
# None -> break
# 1 -> point to None
# return previous


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        previous = head 
        current = head.next 
       
        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp 
        
        head.next = None
        return previous

    
      
            