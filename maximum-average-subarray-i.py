# Leetcode - #643 - Maximum Average Subarray I - https://leetcode.com/problems/maximum-average-subarray-i/description/


# O(n*k)

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average 
# value and return this value. Any answer with a calculation error less than 
# 10-5 will be accepted


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: #[1,12,-5,-6,50,3], k=4

        maxAverage = self.initCurrentAverage(nums, k) # 12,75
        currentAverage = maxAverage
        begin = 1 # 3
        end = k # 6

        while end < len(nums): # 5 < 6
            print(maxAverage)
            leftCut = nums[begin-1]/k if k > 1 else 0
            middleCut = currentAverage if k > 1 else 0
            currentAverage = middleCut - leftCut + nums[end]/k 
            
            maxAverage = max(maxAverage, currentAverage) 

            begin+=1
            end+=1

        return maxAverage

    def initCurrentAverage(self, nums, k):
        avr = 0
        for i in range(k):
            avr += nums[i]

        return avr / k