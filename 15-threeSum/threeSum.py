from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        a + b + c = 0
        :param nums: a list.
        :return: a list.
        """
        ans: List[int] = []
        length: int = len(nums)

        # check boundary
        if None is nums or length < 3:
            return nums

        # log(n)
        nums.sort()

        for i in range(0, length, 1):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            left:int = i + 1
            right:int = length - 1

            while left < right:
               sumValue = nums[i] + nums[left] + nums[right]

               if 0 == sumValue:
                   ans.append([nums[i], nums[left], nums[right]])

                   while left < right and nums[left] == nums[left+1]:
                       left = left + 1
                   while left < right and nums[left] == nums[right-1]:
                       right = right - 1
                   left += 1
                   right -= 1
               elif sumValue < 0:
                   left += 1
               elif sumValue > 0:
                   right -= 1
        return ans
