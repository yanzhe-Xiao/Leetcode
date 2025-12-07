#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start,max_len = 0,0
        def expand_around_center(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1 # 最左边和长度
        for i in range(len(s)):
            l1,len1 = expand_around_center(i,i)
            l2,len2 = expand_around_center(i,i+1)
            if len1 > len2:
                cur_start, cur_len = l1,len1
            else:
                cur_start,cur_len = l2,len2
            if cur_len > max_len:
                max_len = cur_len
                start = cur_start
        return s[start:start+max_len]
# @lc code=end

