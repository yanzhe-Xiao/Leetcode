# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。 
# 
#  算法的时间复杂度应该为 O(log (m+n)) 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
#  
# 
#  Related Topics 数组 二分查找 分治 👍 7814 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 1. 确保 nums1 是较短的那个数组，优化二分效率
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2  # 左半边应该包含的元素总数

        # 2. 在 nums1 上进行二分查找
        left, right = 0, m

        while left <= right:
            # i 是 nums1 的切分点 (包含 i 左边的元素)
            # j 是 nums2 的切分点
            i = (left + right) // 2
            j = total_left - i

            # 处理边界值：如果切分点在最左边，设为负无穷；在最右边，设为正无穷
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]

            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            # 3. 检查交叉条件
            if nums1_left_max > nums2_right_min:
                # nums1 左边的数太大了，i 需要减小
                right = i - 1
            elif nums2_left_max > nums1_right_min:
                # nums2 左边的数太大了 (意味着 nums1 右边太小)，i 需要增大
                left = i + 1
            else:
                # 4. 找到合适的切分点，计算中位数
                if (m + n) % 2 == 1:
                    # 奇数情况：左半边最大的那个就是中位数
                    return max(nums1_left_max, nums2_left_max)
                else:
                    # 偶数情况：(左半边最大 + 右半边最小) / 2
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0

# leetcode submit region end(Prohibit modification and deletion)
