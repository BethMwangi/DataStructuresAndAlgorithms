# @source Leetcode
# Find Pivot Index
# Given an array of integers nums, write a method that returns the "pivot" index of this array.

# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

# Example 1:

# Input: 
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation: 
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.

# Example 2:
# Input: 
# nums = [1, 2, 3]
# Output: -1
# Explanation: 
# There is no index that satisfies the conditions in the problem statement.

# Solution

# Let totalSum be the sum of all the nums. Then we can assume we are at a given index i in the array , we compute the 
# leftSum, sum of all numbers left of index i, then we get the sum of the numbers at right of index as totalSum - num[i] - leftSum



class Solution(object):
    def pivotIndex(self, nums):
        totalSum = sum(nums)
        leftSum = 0

        for i, n in enumerate(nums):
            if leftSum == (totalSum - n - leftSum):
                return i
            leftSum += n
        return -1



# Driver code 

p = Solution()
print(p.pivotIndex([1, 7, 3, 6, 5, 6]))
print(p.pivotIndex([1, 2, 3]))
    




# Complexity Analysis

# Time Complexity: O(N) - N is the length of the nums
# Space Complexity: O(1) -  the space used by leftsum and totalSum