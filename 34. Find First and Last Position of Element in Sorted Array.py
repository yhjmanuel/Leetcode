#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums or nums == []:
            return [-1, -1]
        init = 0
        index_list = []
        while init < len(nums):
            if nums[init] == target:
                index_list.append(init)
            init += 1
        
        if len(index_list) == 1:
            return [index_list[0], index_list[0]]
        else:
            return [index_list[0], index_list[-1]]

