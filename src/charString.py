# -*- coding: UTF-8 -*-
import numpy as np
import re
import collections
"""验证回文字符串,给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        isalnum() 方法检测字符串是否由字母和数字组成
        """
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
"""字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。"""
class Solution1:
    def firstUniqChar(self, s: str) -> int:
        if(len(s)==0):
            return -1
        dic = collections.Counter(s)
        for i in range(0, len(s)):
            if dic[s[i]] < 2:
                return i
        return -1

if __name__ == '__main__':
    """
    a: str = "loveleetcode"
    c = Solution1()
    print(c.firstUniqChar(a))
    """
    lists = ['a', 'a', 'b', '5', '6', '7', '5']
    a = collections.Counter(lists)
    print(a)