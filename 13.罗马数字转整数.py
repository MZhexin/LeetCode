#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start

# 我自己写的丑陋代码
'''
    3999/3999 cases passed (3 ms)
    Your runtime beats 86.59 % of python3 submissions
    Your memory usage beats 39.91 % of python3 submissions (17.4 MB)
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0     # 初始化转换后的数字
        # 建立字母与数字对应的字典
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for index, item in enumerate(s):    # 遍历字符串
            # 几个if判断对应IV、IX、XL、XC、CD、CM这六种特殊情况
            # 结尾的条件 index != 0 杜绝了类似MC这种字符串开头为M，结尾为C，却因为索引问题，将M当做CM来计算的情况（别问，问就是第二次提交时出错了）
            if s[index - 1] == 'I' and item == 'V' and index != 0:
                num -= dict[s[index - 1]]   # 减去之前加上的字母，再加上双字母对应的数 
                num += 4                    # 譬如此处，IV在上一次循环中加了I对应的1，那么这轮循环中，就要减去上轮加上的1，再加上IV代表的4
            elif s[index - 1] == 'I' and item == 'X' and index != 0:
                num -= dict[s[index - 1]]
                num += 9
            elif s[index - 1] == 'X' and item == 'L' and index != 0:
                num -= dict[s[index - 1]]
                num += 40
            elif s[index - 1] == 'X' and item == 'C' and index != 0:
                num -= dict[s[index - 1]]
                num += 90
            elif s[index - 1] == 'C' and item == 'D' and index != 0:
                num -= dict[s[index - 1]]
                num += 400
            elif s[index - 1] == 'C' and item == 'M' and index != 0:
                num -= dict[s[index - 1]]
                num += 900
            else:   # 其他的正常情况都是直接按照字典加就好了
                num += dict[item]
        return num

# 豆包的答案
# 总体思路都是一样的，字典赋值 + 特殊处理首尾元素 + 条件判断特殊情况 + 一般情况直接加减
# 不过豆包是用while循环做的，特殊情况是通过比较两个字符值的数值来计算的，比我的一大串if条件看着优雅多了
# 时间复杂度居然还比我高，哈哈哈哈
'''
    3999/3999 cases passed (7 ms)
    Your runtime beats 55.12 % of python3 submissions
    Your memory usage beats 41.91 % of python3 submissions (17.4 MB)
'''
'''class Solution:
    def romanToInt(self, s: str) -> int:
        # 定义罗马字符和对应数值的映射字典
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        i = 0
        while i < len(s):
            # 如果当前字符是最后一个字符，直接累加其对应数值
            if i == len(s) - 1:
                result += roman_dict[s[i]]
                break
            # 比较当前字符和下一个字符对应的数值
            current_value = roman_dict[s[i]]
            next_value = roman_dict[s[i + 1]]
            if current_value < next_value:
                # 特殊情况，用下一个字符的数值减去当前字符的数值
                result += next_value - current_value
                i += 2
            else:
                # 正常情况，直接累加当前字符的数值
                result += current_value
                i += 1
        return result'''

# @lc code=end

