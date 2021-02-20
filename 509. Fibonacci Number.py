#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        init = [0, 1]
        
        # n-1 operations needed if n > 1
        for i in range(n-1):
            init.append(init[0] + init[1])
            init.pop(0)
        
        return init[-1]

