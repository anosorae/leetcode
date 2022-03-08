#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_map = {}
        for idx, num in enumerate(nums):
            if target - num in dict_map.keys():
                return [idx, dict_map[target-num]]
            else:
                dict_map[num] = idx
        return
# @lc code=end

