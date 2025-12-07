# @before-stub-for-debug-begin
from python3problem12 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        Roman_number = {
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M"
        }
        number_list = list(reversed([1,5,10,50,100,500,1000]))
        
        result = ""
        def minusMaximumValue(num,last_index = 0):
            for index,item in enumerate(number_list[last_index:]):
                if num >= item:
                    num -= item
                    return Roman_number[item],index,num
        li = 0
        while num >= 1:
            ss,li,num = minusMaximumValue(num,li) # type: ignore
            result+=ss
        return result
# @lc code=end

