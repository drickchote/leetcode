# Leetcode - #14 - Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/description/


# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"


# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        firstWord = strs[0]
        for i in range(len(firstWord)):
            for word in strs[1:]:
                if i == len(word) or word[i] != firstWord[i]:
                    return result
            result += firstWord[i]
        
        return result