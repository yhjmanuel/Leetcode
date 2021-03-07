#!/usr/bin/env python
# coding: utf-8

# In[32]:


class Solution:
    def romanToInt(self, s: str) -> int:
        s_dict = {'I': 1, 'V':5, 'X':10, 'L':50,
                'C':100, 'D':500, 'M':1000, 'IV': 4,
                'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM':900}
        
        two_list = ['IV','IX', 'XL', 'XC', 'CD', 'CM']
        
        #this step is important
        s += ' '
        #get all symbols
        symbol_list = [i for i in s]
        #special case
        if len(symbol_list) == 1:
            return s_dict[symbol_list[0]]
        else:
            current = 0
            value = 0
            while current +1 < len(symbol_list):
                curr_symbol = str(symbol_list[current]) + str(symbol_list[current+1])
                #在list中就前移两个位置，否则前移一个
                if curr_symbol in two_list:
                    value += s_dict[curr_symbol]
                    current += 2
                else:
                    value += s_dict[symbol_list[current]]
                    current += 1
            
        
        return value


# In[ ]:




