# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
from collections import defaultdict
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_ = set()
        l = len(s)
        i = j = 0
        if not s:
            return 0
        max_len = 1
        while j < l:
            while s[j] in hash_:
                hash_.remove(s[i])
                i += 1
            hash_.add(s[j])
            max_len = max(max_len,j-i+1)
            j+=1
        return max_len    

                
            
# @lc code=end

