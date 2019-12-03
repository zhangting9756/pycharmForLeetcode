# -*- coding: UTF-8 -*-
import numpy as np
import re

"""验证回文字符串,给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s = re.sub("[^A-Za-z]","",s).lower()

        if s == s[::-1]:

            return True
        else:
            return False


if __name__ == '__main__':
    a: str = "race a car"
    c = Solution()
    print(c.isPalindrome(a))