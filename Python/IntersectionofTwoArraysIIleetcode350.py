# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
from collections import Counter
from typing import List
import numpy as np
#solution1
class Solution1(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        elements_count = Counter(nums1)
        intersection=[]
        for i in nums2:
            if elements_count[i] > 0:
                intersection.append(i)
                elements_count[i] -= 1
        return intersection,elements_count
print('solution1')
print(Solution1().intersect([4,9,5], [9,4,9,8,4]))

#solution2
class Solution2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1=len(nums1)
        n2=len(nums2)
        nums1_sort=sorted(nums1)
        nums2_sort=sorted(nums2)
        intersection_list=[]
        intersection=[]
        i=0
        j=0
        while (i < n1 and j< n2) :
            if nums1_sort[i] == nums2_sort[j]:
                intersection_list.append(nums1_sort[i])
                i+=1
                j+=1
            elif nums1_sort[i] < nums2_sort[j]:
                i=i+1
            else:
                j=j+1
        return intersection_list
print('solution2')
print(Solution2().intersect([4,9,5], [9,4,9,8,4]))