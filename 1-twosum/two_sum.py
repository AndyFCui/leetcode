from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        This is two sum demo.
        :param nums: list of number.
        :param target: target number.
        :return: answer is two value [i, j]
        """
        # use dict same as `indices = dict()` which is HashMap function
        indices = {}

        for i in range(0, len(nums), 1):
            indices[nums[i]] = i

        for i in range(0, len(nums), 1):
            diff: int = target - nums[i]
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        return []

    # This algo time complex is O(n) + O(n) = O(n)

"""
For this problem we use greedy algo, since we create a data structure 
like HashMap to store a indexed list, then we use diff to match list value,
if exist the two value, then we return the current i and matched HashMap keyValue.  
"""