// Neetcode 125 - https://leetcode.com/problems/valid-palindrome/description/

#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        int strSize = size(s);
        int firstIndex = 0;
        int lastIndex = strSize - 1;

        for(int i=0; i< (int)(strSize /2); i++){
            while (firstIndex < s.size() &&
            !std::isalnum(static_cast<unsigned char>(s[firstIndex]))) {
                firstIndex++;
            }

            while (lastIndex >= 0 &&
            !std::isalnum(static_cast<unsigned char>(s[lastIndex]))) {
                lastIndex--;
            }
            

            if(firstIndex > lastIndex){
                return true;
            }

            char a = std::tolower(static_cast<unsigned char>(s[firstIndex]));
            char b = std::tolower(static_cast<unsigned char>(s[lastIndex]));

            if(a != b){
                return false;
            }

            firstIndex++;
            lastIndex--;
        }

        return true;
    }
};