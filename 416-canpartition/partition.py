from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        This is for partition equal subset sum.
        :param nums: numbers
        :return: true or false.
        """
        total = sum(nums)
        if total & 1:
            return False
        n = len(nums)

        target = total // 2

        dp = [[False] * (target + 1) for _ in range(n)]

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(0, target + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i] == j:
                    dp[i][j] = True
                    continue

                if nums[i] < j:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]

        return dp[n - 1][target]