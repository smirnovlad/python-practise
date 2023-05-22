from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        if 1 not in nums:
            return 0
        result = 0
        left_length, right_length = 0, 0
        for pos, el in enumerate(nums):
            if el == 0:
                if pos > 0 and nums[pos - 1] == 0:
                    left_length = 0
                    continue
                result = max(result, left_length + right_length)
                left_length = right_length
                right_length = 0
            else:
                right_length += 1
        result = max(result, left_length + right_length)
        return result
