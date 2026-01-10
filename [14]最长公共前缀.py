# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] 如果非空，则仅由小写英文字母组成 
#  
# 
#  Related Topics 字典树 数组 字符串 👍 3443 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if not strs:
        #     return ""
        # prefix = strs[0]
        # for ss in strs:
        #     while not ss.startswith(prefix):
        #         prefix = prefix[:-1]
        #         if not prefix:
        #             return ""
        # return prefix
        def lcp(str1, str2):
            length = min(len(str1), len(str2))
            index = 0
            while index < length and str1[index] == str2[index]:
                index += 1
            return str1[:index]
        if not strs:
            return ""
        for i in range(1, len(strs)):
            strs[0] = lcp(strs[0], strs[i])
            if not strs[0]:
                return ""
        return strs[0]
# leetcode submit region end(Prohibit modification and deletion)
