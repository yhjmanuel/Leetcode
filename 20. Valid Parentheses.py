#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isValid(self, s: str) -> bool:
        str_list = [i for i in s]
        front = []
        for i in str_list:
            if i in ['(','[','{']:
                front.append(i)
            elif i in [')',']','}']:
                if front and front[-1] + i in ['()','[]','{}']:
                    front.pop()
                else:
                    return False
        
        return front == []

