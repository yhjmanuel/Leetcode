#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#切片用法举例
#a='python'
#b=a[::-1]
#print(b) #nohtyp
#c=a[::-2]
#print(c) #nhy
#从后往前数的话，最后一个位置为-1
#d=a[:-1]  #从位置0到位置-1之前的数
#print(d)  #pytho
#e=a[:-2]  #从位置0到位置-2之前的数
#print(e)  #pyth


class Solution:
    def addTwoNumbers(self, l1, l2):
        
        l1_num = str(l1.val)
        while l1.next:
            l1_num += str(l1.next.val)
            l1 = l1.next
        l1_num = int(l1_num[::-1])
        
        l2_num = str(l2.val)
        while l2.next:
            l2_num += str(l2.next.val)
            l2 = l2.next
        l2_num = int(l2_num[::-1])
        
        l1_l2_sum = str(int(l1_num) + int(l2_num))

        len_sum = len(l1_l2_sum)
        result = ListNode(int(l1_l2_sum[0]))
        for i in range(1, len_sum):
            result = ListNode(int(l1_l2_sum[i]), result)
        
        return result

