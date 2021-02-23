#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)

        length = len(nums)
        length_half = length / 2
        if length % 2 == 0:
            return (nums[int(length_half)] + nums[int(length_half)  - 1]) / 2
        else:
            position = int(length_half)
            return nums[position]

