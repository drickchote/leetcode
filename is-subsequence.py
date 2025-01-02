# Leetcode - #392 - Is Subsequence - https://leetcode.com/problems/is-subsequence/description/

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

#O(n) 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subStrIndex = 0 
        targetIndex = 0

        while targetIndex < len(t) and subStrIndex < len(s): 
            if t[targetIndex] == s[subStrIndex]:
                subStrIndex+=1
            targetIndex+=1

        return subStrIndex == len(s)
        