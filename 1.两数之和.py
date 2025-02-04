#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

# 自己做的答案（穷举法）
'''
    63/63 cases passed (1925 ms)
    Your runtime beats 12.05 % of python3 submissions
    Your memory usage beats 57.42 % of python3 submissions (18 MB)
'''
'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []    # 创建新列表
        for index1, item1 in enumerate(nums):   # 从头开始遍历第一遍数组，找到第一个数
            for index2 in range(index1 + 1, len(nums)):  # 从第一个数的下一个数开始，遍历第二遍数组，找到第二个数
                if item1 + nums[index2] == target:  # 如果两数相加为目标数
                    ans.append(index1)  # 两个数依次存入列表并返回
                    ans.append(index2)
        return ans'''


# 参考豆包给出的优化后，自己写的版本（使用哈希算法，即Python字典)
# 可以明显看到，时间复杂度降低了，但空间复杂度变高了（哈希算法要用更多的内存空间解决冲突问题）
'''
    63/63 cases passed (0 ms)
    Your runtime beats 100 % of python3 submissions
    Your memory usage beats 8.91 % of python3 submissions (18.8 MB)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}   # 建立空字典
        for index, item in enumerate(nums): # 遍历所有数
            # 注意：这里不能把存入字典的操作写在这里。如果某个item刚好是target的一半，那么先存再检索就会把自己算两次，而题目不允许重复计算数字
            distance = target - item    # 计算当前这个数加上几等于目标
            if distance in num_dict:    # 在字典里找有没有缺的数，有就直接返回，没有就进入下一轮循环
                return [num_dict[distance], index]
            num_dict[item] = index  # 每遇到一个数就存入字典


# 豆包给出的答案
'''class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 创建一个空字典，用于存储元素及其索引
        num_dict = {}
        for i, num in enumerate(nums):
            # 计算当前元素与目标值的差值
            complement = target - num
            # 检查差值是否在字典中
            if complement in num_dict:
                # 如果差值在字典中，返回差值的索引和当前元素的索引
                return [num_dict[complement], i]
            # 将当前元素及其索引存入字典
            num_dict[num] = i'''

# @lc code=end
