# Leetcode - #116 - Populating Next Right Pointers in Each Node 
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/


#You are given a perfect binary tree where all leaves are on the same level,
#and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. 
# If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.



class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        queue = [root] # [  None, None, None, None, None, None, None, None]
        level = 0 # 3
        levelLastIndex = 2 ** level # 15
        index = 1 # 8

        while queue[0] is not None:
            element = queue.pop(0) 
            
            if index < levelLastIndex:
                element.next = queue[0]
            else:
                level+= 1 
                levelLastIndex += 2 ** level

            index+=1
            queue.append(element.left)
            queue.append(element.right)
        
        return root

            
