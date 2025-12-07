# @before-stub-for-debug-begin
from python3problem6 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lists = [[] for i in range(numRows)]
        # print(lists)
        index_list = []
        for i in range(numRows + numRows - 2):
            if i < numRows:
                index_list.append(i)
            else:
                index_list.append(numRows - 2 -(i - numRows))
        segmentation = len(index_list)
        for index,item in enumerate(s):
            cur_index_list = index_list[index % segmentation]
            lists[cur_index_list].append(item)
        result = ''.join([''.join(lst) for lst in lists])
        return result
# @lc code=end

