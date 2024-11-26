# Leetcode - #5 - Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

# Given a string s, return the longest  palindromic substring in s

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Solution:
# loop through all letters and expand 
# idea: if s is a palindrome so 'x' + s + 'x' is also a palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        
        for i in range(0, len(s)):
            ## even length
            current = ""
            limit = 0
            while self.isSafe(s, i-limit, i+limit+1) and s[i-limit] == s[i+limit+1]:
                limit+= 1
            
            if limit > 0:
                limit -= 1
                current = s[i-limit:i+limit+2]
                longest = self.biggerString(longest, current)

            ## odd length
            limit = 1
            while self.isSafe(s, i-limit, i+limit) and s[i-limit] == s[i+limit]:
                limit+=1

            if limit > 1:
                limit -= 1
                current = s[i-limit:i+limit+1]
                longest = self.biggerString(longest, current)
        
        return longest

    def isSafe(self, string, lower, upper):
        return lower >= 0 and upper < len(string)

    def biggerString(self, s1, s2):
        return s1 if len(s1) >= len(s2) else s2