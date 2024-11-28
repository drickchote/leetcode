# Leetcode - #61 - Rotate List - https://leetcode.com/problems/rotate-list/description/

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        length = 1
        current = head
        # Go to the last element, save tail and count
        while current.next != None:
            current = current.next
            length +=1
        tail = current 
        tail.next = head # conect the old tail to the head

        k =  k % length # ensure not rotate more than necessary
        newTailIndex = length - k -1 # index of the new tail

        current = head
        for i in range(newTailIndex): # Go to the new tail
            current = current.next
        
        head = current.next
        current.next = None

        return head



        

        