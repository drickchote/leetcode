# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0

        for i in range(len(s)):
            longest = max(longest, self.calculate(s[i:]))
        
        return longest


    def calculate(self, s) -> str:
        longest = ""

        for i in range(len(s)):
            x = s[i]
            if x in longest:
                break

            longest+=x
        return len(longest)
        