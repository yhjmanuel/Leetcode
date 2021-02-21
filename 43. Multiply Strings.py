#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        len_num1 = len(num1)
        len_num2 = len(num2)

        num1_sum = 0
        num2_sum = 0

        for i in range(len_num1):
            num1_sum += int(num1[::-1][i]) * (10 ** i)
        
        for i in range(len_num2):
            num2_sum += int(num2[::-1][i]) * (10 ** i)
        
        return str(num1_sum * num2_sum)

