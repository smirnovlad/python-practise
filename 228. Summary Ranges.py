from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        result = []
        firstPos = 0
        for lastPos in range(1, len(nums)):
            if nums[lastPos] - nums[lastPos - 1] != 1:
                if firstPos + 1 == lastPos:
                    result.append("{}".format(nums[firstPos]))
                else:
                    result.append("{}->{}".format(nums[firstPos], nums[lastPos - 1]))
                firstPos = lastPos
        if firstPos == len(nums) - 1:
            result.append("{}".format(nums[firstPos]))
        else:
            result.append("{}->{}".format(nums[firstPos], nums[lastPos]))
        return result