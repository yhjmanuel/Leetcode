#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        init = 0
        while init < len(nums):
            if nums[init] >= target:
                return init
            init += 1
        
        return len(nums)

