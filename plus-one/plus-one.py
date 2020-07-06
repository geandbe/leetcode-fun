# Leetcode Problem 66 - Plus One (easy)
# https://leetcode.com/problems/plus-one/
# FUNCTIONAL SOLUTION
# Unpublished Work © 2020 Gene Belitski
import unittest
from typing import List


class SolutionA:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))


class SolutionB:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(digit) for digit in str(int(''.join(map(str, digits))) + 1)]


class SolutionC:
    def plusOne(self, digits: List[int]) -> List[int]:
        def add_one(pos: int) -> List[int]:
            if digits[pos] < 9:
                digits[pos] += 1
                return digits
            else:
                digits[pos] = 0
                return [1] + digits if not pos else add_one(pos - 1)

        return add_one(len(digits) - 1)


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [1] if not digits else \
            digits[:-1] + [digits[-1] + 1] if digits[-1] < 9 else \
            self.plusOne(digits[:-1]) + [0]


class TestSolution(unittest.TestCase):
    def test_carry_on(self):
        self.assertEqual([1, 0], Solution().plusOne(digits=[9]))

    def test_zero(self):
        self.assertEqual([1], Solution().plusOne(digits=[0]))

    def test_example_1(self):
        self.assertEqual([1, 2, 4], Solution().plusOne(digits=[1, 2, 3]))

    def test_example_2(self):
        self.assertEqual([4, 3, 2, 2], Solution().plusOne(digits=[4, 3, 2, 1]))


if __name__ == '__main__':
    unittest.main()
