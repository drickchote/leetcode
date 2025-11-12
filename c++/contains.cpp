// 217. Contains Duplicate
#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, bool> memo;

        for (int num: nums){
            if(memo.find(num) != memo.end()){
                return true;
            }
            memo[num] = true;
        }
        return false;
    }
};