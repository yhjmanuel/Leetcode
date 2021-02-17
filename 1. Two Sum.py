#!/usr/bin/env python
# coding: utf-8

# In[67]:


class Solution:
    def twoSum(self, nums, target):
        len_list = len(nums)
        for i in range (len_list):
            current_number = nums[i]
            left_number = target - current_number
            if left_number in nums[i+1:]:
                del nums[i]
                return [i , nums.index(left_number)+1]

