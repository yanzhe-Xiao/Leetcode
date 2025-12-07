# @before-stub-for-debug-begin
from python3problem8 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s :
            return 0
        num_str = ""
        flag = -1 # 默认为正
        nums = ['1','2','3','4','5','6','7','8','9','0']
        for index,ss in enumerate(s):
            if not num_str:
                if ss == " " :
                    if flag != -1:
                        return 0
                    continue
                elif ss == "-" :
                    if flag != -1:
                        return 0
                    flag = 1
                    continue
                elif ss == "+" :
                    if flag != -1:
                        return 0
                    flag = 0
                    continue
                elif ss not in nums:
                    return 0
            elif ss not in nums:
                break
            num_str += ss
        if not num_str:
            return 0
        result = int(num_str)
        result = result if flag == 0 or flag == -1 else -result 
        max_num = 2**31 - 1
        min_num = -2**31
        result = min(result,max_num)
        result = max(result,min_num)
        return result   

# @lc code=end

