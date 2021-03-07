#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def removeDuplicates(self, nums) -> int:
        a = 0
        b = 1
        while b < len(nums):
            if nums[b] == nums[a]:
                nums.pop(a)
            else:
                a += 1
                b += 1
        return len(nums)

