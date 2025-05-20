# Leetcode - #700 - Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/description

# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree 
#rooted with that node. If such a node does not exist, return null.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# BCR: 
# -> Time: O(log n)
# -> Space: O(1)

# First Try:
# -> Time: O(log n)
# -> Space: O(1)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        
        while current != None and current.val != val:
            if current.val > val:
                current = current.left
            else: 
                current = current.right

        return current