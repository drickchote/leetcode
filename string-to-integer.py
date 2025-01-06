# Leetcode - #8 - String to Integer (atoi) - https://leetcode.com/problems/string-to-integer-atoi/description/


# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+',
# assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered
#  or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
# then round the integer to remain in the range. Specifically, 
# integers less than -231 should be rounded to -231, and integers greater than 231 - 1 
# should be rounded to 231 - 1.
# Return the integer as the final result.

class Solution:

    def __init__(self):
        self.numbers = {"0":0 , "1":1 , "2":2 , "3":3 , "4":4 , "5":5 , "6":6 , "7":7 , "8":8 , "9": 9}

    def myAtoi(self, s: str) -> int:
        result = 0
        signal = 1

        i = 0
        while i < len(s) and (s[i] == " " or s[i] == 0):
            i+=1
        return s

        if len(s) == i+1:
            return result
        
        if s[i] == '-':
            signal = -1
            i+=1
        elif s[i] == '+':
            i+=1
        

        stack = []

        j = 0
        while j < len(s) and self.numbers.get(s[j]) is not None:
            stack.append(self.numbers[s[j]])
            j+=1

        while len(stack) != 0:
            topElement = stack.pop(0)
            result += topElement * 10 ** len(stack)

        result *= signal

        if result >= 2 ** 31:
            return 2**31 -1
        
        if result < -1 * 2 ** 31:
            return -1 * 2 ** 31
        
        return result
            