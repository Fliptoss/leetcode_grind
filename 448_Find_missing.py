# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.



# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]


# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # create a set and put a copy of the array inside the set
        # rem [] will be placed inside the set

        seen = set(nums)
        rem = []

        for i in range(1, len(nums)+1):
            if i not in seen:
                rem.append(i)

        return rem
        # time complexity O(n)
        # space complexity O(n)
