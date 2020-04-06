# @source Leetcode
# In a given integer array nums, there is always exactly one largest element.

# Find whether the largest element in the array is at least twice as much as every other number in the array.

# If it is, return the index of the largest element, otherwise return -1.

# Example 1:

# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

# Example 2:

# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
#

class Solution:
    def dominantIndex(self, nums):

        maxIndex = 0

        for i in range(0, len(nums)):
            if nums[i] > nums[maxIndex]:
                maxIndex = i

        for i in range(0, len(nums)):
            if maxIndex != i and nums[maxIndex] < (2 * nums[i]):
                return -1
        return maxIndex


# Driver code 
p = Solution()
print(p.dominantIndex([3, 6, 1, 0]))
print(p.dominantIndex([1, 2, 3, 4]))


# Complexity Analysis

# Time Complexity: O(N) where N is the length of nums.

# Space Complexity: O(1) the space used by our int variables.