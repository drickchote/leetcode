
# Leetcode - #1346 - Check if N and Its Double Exists - https://leetcode.com/problems/check-if-n-and-its-double-exist/description/


# Given an array arr of integers, check if there exist two indices i and j
# such that:

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool: # [10,2,5,3]
        alreadyVisited = {} # []

        for element in arr: 
            if alreadyVisited.get(element * 2) is not None or alreadyVisited.get(element / 2) is not None :
                return True 
            alreadyVisited[element] = 1
        return False