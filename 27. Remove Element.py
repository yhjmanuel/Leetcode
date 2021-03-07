#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        b = 0
        #注意下面是len(nums),是动态的量；不要提前令length = len(nums),然后用while b<length
        while b < len(nums):
            if nums[b] == val:
                nums.pop(b)
            else:
                b += 1
        
        return len(nums)

