#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calVolume(left,right):
            return (right-left)*min(height[right],height[left])
        area = 0
        i,j = 0,len(height)-1
        while i < j:
            area = max(calVolume(i,j),area)
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
            
# @lc code=end

