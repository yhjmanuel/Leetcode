#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == '-':
            result = int(str(x)[1:][::-1]) * -1
            if -2147483648 < result < 2147483647:
                return result
            else:
                return 0
                
        else:
            result = int(str(x)[::-1])
            if -2147483648 < result < 2147483647:
                return result
            else:
                return 0

