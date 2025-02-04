#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start

# 我自己写的
'''
    11511/11511 cases passed (22 ms)
    Your runtime beats 6.6 % of python3 submissions
    Your memory usage beats 6.28 % of python3 submissions (17.7 MB)
'''
'''class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = [] # 创建空列表
        for index, item in enumerate(str(x)):   # 将数字转换为字符串后遍历
            ans.append(item)    # 将每一位数存入列表
        if ans == ans[::-1]:    # 判断列表是否等于列表的倒序（即数是否回文）
            return True
        else:
            return False'''
        
# 看了豆包之后自己写的
# 思路：纯数学知识判断，譬如以哪些数结尾不可能是回文数等规则进行判断。空间复杂度为常数级
'''
    11511/11511 cases passed (8 ms)
    Your runtime beats 53.34 % of python3 submissions
    Your memory usage beats 12.35 % of python3 submissions (17.7 MB)
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 纯数学判断
        if x != 0 and x % 10 == 0:  # 以0结尾的非0数：非回文数
            return False
        elif x < 0:     # 小于0的数：非回文数（考虑负号）
            return False
        
        # 用数位判断：不断将原数去掉最后一位，将翻转的数添加最后一位，判断二者是否相等
        reversed_num = 0  # 初始化翻转的数，准备比较
        original_num = x

        # 如果翻转数比原数小（即数位少），表示还没有完全将原数对半分，需要继续循环
        while reversed_num < original_num:
            num = original_num % 10     # 取出原数的最后一位
            reversed_num *= 10          # 翻转的数往后添一位
            reversed_num += num 
            original_num //= 10         # 原数去掉最后一位

        # 比较原数和翻转数：分奇偶两种情况（奇数的话中间多一位）
        if original_num == reversed_num or original_num == reversed_num // 10:
            return True
        else:
            return False

# 豆包写的答案
'''
    11511/11511 cases passed (7 ms)
    Your runtime beats 65.77 % of python3 submissions
    Your memory usage beats 39.94 % of python3 submissions (17.4 MB)
'''
'''class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数和以 0 结尾但不是 0 的数一定不是回文数
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        while x > reversed_num:
            # 取出 x 的最后一位数字
            digit = x % 10
            # 将取出的数字添加到 reversed_num 中
            reversed_num = reversed_num * 10 + digit
            # 去掉 x 的最后一位数字
            x = x // 10

        # 当数字长度为奇数时，reversed_num 的中间数字不需要比较，直接去掉中间数字进行比较
        return x == reversed_num or x == reversed_num // 10'''

# 豆包的优化建议
'''
    1、可以简化 if - else 语句，直接返回布尔表达式的结果，可以减少代码量，并且可能在一定程度上提高执行效率；
    2、去除额外变量 original_num ，直接使用 x 进行操作，可以减少内存开销。
'''

# @lc code=end

