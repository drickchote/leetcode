
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int initial = 0;
        int end = nums.size()-1;
        while(initial <= end){
            int pivot = (int)(initial+end)/2;
            if(nums[pivot] == target){
                return pivot;
            } 

            if(nums[pivot] > target){
                end = pivot-1; 
            } else {
                initial = pivot + 1;
            }
        }
        return -1;
    }
};
