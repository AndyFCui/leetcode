from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        This is two sum demo.
        :param nums: list of number.
        :param target: target number.
        :return: answer is two value [i, j]
        """
        # use dict same as `indices = dict()` which is mashMap function
        indices = {}
        
        for i in range(0, len(nums), 1):
            indices[nums[i]] = i

        for i in range(0, len(nums), 1):
            diff: int = target - nums[i]
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        return []

    # This algo time complex is O(n) + O(n) = O(n)
