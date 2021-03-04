#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        length = 201
        for string in strs:
            if len(string) < length:
                length = len(string)
                shortest_str = string
        prefix = ''
        for i in range(length):
            for string in strs:
                if string[i] != shortest_str[i]:
                    return prefix
            prefix += shortest_str[i]

        return prefix

