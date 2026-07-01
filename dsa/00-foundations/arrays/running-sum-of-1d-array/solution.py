from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result: List[int] = []
        current_sum = 0

        for num in nums:
            current_sum += num
            result.append(current_sum)

        return result
