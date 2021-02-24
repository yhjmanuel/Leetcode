#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        p1 = 0
        p2 = length - 1
        max_size = min(height[p1], height[p2]) * (length - 1)
        length -= 1
        while p1 != p2:
            if min(height[p1], height[p2]) == height[p1]:
                #说明是p1一端比较短
                p1 += 1
                length -= 1
                new_size = length * min(height[p1], height[p2])
                if new_size > max_size:
                    max_size = new_size
            else:
                p2 -= 1
                length -= 1
                new_size = length * min(height[p1], height[p2])
                if new_size > max_size:
                    max_size = new_size
        
        return max_size

