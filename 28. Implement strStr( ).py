#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #sliding windows
        len1 = len(haystack)
        len2 = len(needle)
        for i in range(len1- len2 +1):
            if haystack[i:i+len2] == needle:
                return i
        
        return -1

