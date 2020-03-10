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
"""实现 strStr()
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。"""
class Solution4:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if haystack == needle:
            return 0
        if needle not in haystack:
            return -1
        else:
            h = haystack.split(needle)
            return len(h[0])
"""最长公共前缀"""
class Solution5(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """
        # 判断是否为空
        if not strs:
            return ''
        # 在使用max和min的时候已经把字符串比较了一遍
        # 当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最小的字符串
        s1 = min(strs)
        # 当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最大的字符串
        s2 = max(strs)
        # 使用枚举变量s1字符串的每个字母和下标
        for i, c in enumerate(s1):
            # 比较是否相同的字符串，不相同则使用下标截取字符串
            if c != s2[i]:
                return s1[:i]
        return s1
        """
        import os
        return os.path.commonprefix(strs)
"""有效的括号"""
class Solution6:
    def isValid(self, s):
        pre_dict = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in pre_dict.values():  # 表明i为左括号，入栈
                stack.append(i)
            # i为右括号，若此时栈空(not stack)或者与出栈的不匹配则
            # 匹配出错 ，return False
            elif not stack or pre_dict[i] != stack.pop():
                return False
        return not stack  # 若结束时栈空则return True,反之return False
"""二叉树的层次遍历"""
class Solution7:
    def levelOrder(self,root):
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels

"""将有序数组转换为二叉搜索树，用到二叉查找法"""
class Solution8:
    def _sortedArrayToBST(self, nums, start, end):
        if start > end:
            return None

        mid = (end - start)//2 + start
        midNode = TreeNode(nums[mid])
        midNode.left = self._sortedArrayToBST(nums, start, mid - 1)
        midNode.right = self._sortedArrayToBST(nums, mid + 1, end)
        return midNode
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self._sortedArrayToBST(nums, 0, len(nums) - 1)

if __name__ == '__main__':

    a ="()[]{}"
    b = "ll"
    c = Solution6()
    print(c.isValid(a))

