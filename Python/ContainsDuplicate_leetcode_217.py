# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Solution1: time complexity O(n^2)
class Solution1(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i=0
        j=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
# Solution 2: time complexity O(nlogn)
class Solution2(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums=sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
# Solution 3: time complexity O(n) because of set()
class Solution3(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums))<len(nums)
print(Solution1().containsDuplicate([1,2,3,1])) # True
print(Solution2().containsDuplicate([1,2,3,1])) # True
print(Solution3().containsDuplicate([1,2,3,1])) # True