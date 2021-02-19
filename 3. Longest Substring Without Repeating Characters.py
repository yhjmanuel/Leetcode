#!/usr/bin/env python
# coding: utf-8

# In[32]:


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_str = len(s)
        largest_len = 0
        a = []
        for i in range(len_str):
            if s[i] not in a:
                a.append(s[i])
            else:
                if len(a) > largest_len:
                    largest_len = len(a)
                while s[i] in a:
                    a.pop(0)
                a.append(s[i])
        
        if len(a) > largest_len:
            largest_len = len(a)
        
        return largest_len

