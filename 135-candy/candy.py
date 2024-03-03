from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Fill all kinds init 1 candy.
        candies: List = [1 for _ in range(len(ratings))]

        # From left to right
        for i in range (1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Record the right side value
        result: int = candies[-1]

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i + 1] + 1, candies[i])

            result += candies[i]

        return result
