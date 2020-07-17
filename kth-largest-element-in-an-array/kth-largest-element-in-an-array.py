# Leetcode Problem 215 - Kth Largest Element in an Array  (medium)
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# FUNCTIONAL SOLUTION
# Unpublished Work © 2020 Gene Belitski
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


assert Solution().findKthLargest([3, 2, 1,5, 6, 4], 2) == 5
assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert Solution().findKthLargest([1], 1) == 1
