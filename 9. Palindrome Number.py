#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

