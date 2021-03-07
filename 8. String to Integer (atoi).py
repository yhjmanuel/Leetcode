#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def myAtoi(self, s: str) -> int:
        num_list = [f'{i}' for i in range(10)]
        number = []
        char_list = [char for char in s]
        #delete whitespace if any
        while char_list and char_list[0] == ' ':
            char_list.pop(0)

        #determine whether a symbol exists
        if char_list:
            if char_list[0] == '-':
                symbol = -1
                char_list.pop(0)
            elif char_list[0] == '+':
                symbol = 1
                char_list.pop(0)
            else:
                symbol = 1
            
        #put all numbers in the list 
            while char_list and char_list[0] in num_list:
                number.append(char_list[0])
                char_list.pop(0)
            if number:
                index = 0
                power = len(number) - 1
                value = 0
                while index < len(number):
                    value += int(number[index]) * 10 ** power
                    index += 1
                    power -= 1

                if value *  symbol > 2 **31 -1 :
                    return 2 **31 -1
                elif value * symbol < - 2 **31 :
                    return -2 ** 31
                else:
                    return value * symbol

        return 0

