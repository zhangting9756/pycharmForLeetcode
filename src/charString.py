# -*- coding: UTF-8 -*-
import numpy as np
import re
import collections
import operator
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
"""给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。"""
class Solution2:
    def reverse(self, x: int) -> int:
        num = 0
        if x == 0:
            return 0
        if x < 0:
            x = -x
            while x != 0:
                num = num * 10 + x % 10
                x = int(x / 10)
            num = -num
        else:
            while x != 0:
                num = num * 10 + x % 10
                x = int(x / 10)

        if num > pow(2, 31) - 1 or num < pow(-2, 31):
            return 0
        return num
"""给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。"""
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        length1=len(s)
        length2=len(t)
        if(length1 != length2):
            return False
        dic1 = collections.Counter(s)
        dic2 = collections.Counter(t)
        """
        for i in range(0, len(s)):
            if(dic1[s[i]]!=dic2[s[i]]):
                return False
                
        operator.lt(a, b)   //a<b
        operator.le(a, b)   //a<=b
        operator.eq(a, b)   //a==b
        operator.ne(a, b)   //a!=b
        operator.ge(a, b)   //a>=b
        operator.gt(a, b)   //a>b
        """
        return operator.eq(dic1,dic2)

if __name__ == '__main__':
    """
    a: str = "loveleetcode"
    c = Solution1()
    print(c.firstUniqChar(a))
    """
    lists = ['a', 'a', 'b', '5', '6', '7', '5']
    a = Solution3()
    print(a.isAnagram("rat","car"))