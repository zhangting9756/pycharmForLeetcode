# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

"""买卖股票的最佳时机 II"""


class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        if (prices):

            for i in range(len(prices) - 1):
                if (prices[i + 1] > prices[i]):
                    maxProfit += prices[i + 1] - prices[i]
            return maxProfit
        else:
            return 0


"""从排序数组中删除重复项 """


class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums):
            count = 1
            temp = nums[0]
            for i in range(len(nums)):
                if (temp != nums[i]):
                    nums[count] = nums[i]
                    temp = nums[i]
                    count = count + 1
            return count
        else:
            return 0


class Solution3:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            k = k % len(nums)
            nums[:] = nums[-k:] + nums[:-k]


""" 存在重复"""


class Solution4:
    def containsDuplicate(self, nums):
        a = len(nums)
        b = len(set(nums))
        if (a != b):
            return True
        else:
            return False


"""只出现一次的数字 """


class Solution5:
    def singleNumber(self, nums):
        res = 0
        for i in nums:
            res ^= i
        return res


"""   两个数组的交集 II"""


class Solution6:
    def intersect(self, nums1, nums2):
        if (nums1):
            if (nums2):
                ret = []
                ret = [i for i in nums1 if i in nums2]
        return ret


"""加一"""


class Solution7:
    def plusOne(self, digits):

        i=len(digits)-1
        carry=1
        while i>=0:
            digits[i]=digits[i]+carry
            if(digits[i]>9):
                digits[i]=digits[i]-10
                carry=1
            else:
                carry=0
                break
            i=i-1
        if carry==1:
            digits.insert(0,1)
        return digits
        """
        i = len(digits) - 1
        while i > 0 and digits[i] == 9:
            digits[i] = 0
            i = i - 1
        if i == 0 and digits[0] == 9:
            digits[0] = 0
            digits.insert(0, 1)
        else:
            digits[i] = digits[i] + 1
        return digits
        """

""" 移动零 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。"""


class Solution8:
    def moveZeroes(self, nums):
        """
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
        """
        """
        count, length  = 0, len(nums)
        while count != length:
            if nums[count] == 0:
                del nums[count]
                nums.append(0)
                count -= 1
                length -= 1
            count += 1   
        """
        idxs = [idx for idx, num in enumerate(nums) if num == 0]
        for i in idxs[::-1]:
            nums.pop(i)
        nums += len(idxs) * [0]


"""两数之和 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。"""


class Solution9:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in dict:
                return dict[a], i
            else:
                dict[nums[i]] = i

"""旋转图像"""
class Solution10:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            for j in range(i + 1, length):
                temp = matrix[i, j]
                matrix[i, j] = matrix[j, i]
                matrix[j, i] = temp
        for i in range(length):
            matrix[i] = matrix[i][::-1]

"""字符串翻转"""
class Solution11:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
"""丑数"""
class Solution12:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        # 1作为特殊数直接保存
        baselist = [1]
        min2 = min3 = min5 = 0
        curnum = 1
        while curnum < index:
            minnum = min(baselist[min2] * 2, baselist[min3] * 3, baselist[min5] * 5)
            baselist.append(minnum)
            # 找到第一个乘以2的结果大于当前最大丑数M的数字，也就是T2
            while baselist[min2] * 2 <= minnum:
                min2 += 1
            # 找到第一个乘以3的结果大于当前最大丑数M的数字，也就是T3
            while baselist[min3] * 3 <= minnum:
                min3 += 1
            # 找到第一个乘以5的结果大于当前最大丑数M的数字，也就是T5
            while baselist[min5] * 5 <= minnum:
                min5 += 1
            curnum += 1
        return baselist[-1]
"""合并两个有序数组
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。"""
class Solution13:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m > 0 and n == 0:
            nums1 = nums1
        for i,num in enumerate(nums2):
            nums1[-(i+1)] = num
        nums1 = nums1.sort()

if __name__ == '__main__':
    a = [1,2,3,0,0,0]
    b=[2,5,6]
    print("hello1")
    # b = input()
    print("hello2")
    c = Solution13()
    c.merge(a,3,b,3)
    print(a)


