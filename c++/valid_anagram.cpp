// 242 - Valid anagram - https://leetcode.com/problems/valid-anagram

#include <iostream>
#include <string>
#include <map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }

        unordered_map<char, int> m;

        for (int i = 0; i < s.size(); i++){
            m[s[i]]++;
        }

        for (int i = 0; i < s.size(); i++){
            if(m[t[i]] == 0){
                return false;
            }

            m[t[i]]--;
        }

        return true;
    }
};

int main(){
    Solution solution = {};

    cout << solution.isAnagram("car", "rat") << endl;
}