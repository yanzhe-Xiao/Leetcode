# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[
# b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）： 
# 
#  
#  0 <= a, b, c, d < n 
#  a、b、c 和 d 互不相同 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  你可以按 任意顺序 返回答案 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics 数组 双指针 排序 👍 2127 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
        def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            nums.sort()
            n = len(nums)
            res = []
            for i in range(n - 3):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                # 剪枝：最小和已经大于 target
                if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                    break
                # 剪枝：当前 nums[i] 太小，最大和仍小于 target
                if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                    continue
                for j in range(i + 1, n - 2):
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        continue
                    if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                        break
                    if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                        continue
                    left, right = j + 1, n - 1
                    while left < right:
                        s = nums[i] + nums[j] + nums[left] + nums[right]
                        if s == target:
                            res.append([nums[i], nums[j], nums[left], nums[right]])
                            left += 1
                            right -= 1
                            while left < right and nums[left] == nums[left - 1]:
                                left += 1
                            while left < right and nums[right] == nums[right + 1]:
                                right -= 1
                        elif s < target:
                            left += 1
                        else:
                            right -= 1
            return res
# leetcode submit region end(Prohibit modification and deletion)
