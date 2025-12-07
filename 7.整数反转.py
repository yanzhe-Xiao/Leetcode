# @before-stub-for-debug-begin
from python3problem7 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # 1. 取符号
        sign = 1 if x >= 0 else -1
        
        # 2. 取绝对值 -> 转字符串 -> 反转 -> 转回整数
        # int() 会自动处理反转后字符串开头的 '0' (例如 "021" -> 21)
        reversed_x = int(str(abs(x))[::-1])
        
        # 3. 恢复符号
        result = reversed_x * sign
        
        # 4. 检查 32 位整数溢出
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result
# @lc code=end

