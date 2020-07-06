Apparently if the last element of `digits` is less, than `9`, the solution is just the same list with the last element incremented by one, or `digits[:-1] + [digits[-1] + 1]`.

If the last of `digits` equals `9` the solution is the solution for the original list without the last element, or `self.plusOne(digits[:-1])` appended by `0`, or `self.plusOne(digits[:-1]) + [0]`.

Finally, what if original list of digits by subsequent decreasing in size gets empty? In this case we just need to return leftover carry-on [1].

Putting the above together gives an elegant one-statement solution:
```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [1] if not digits else \
            digits[:-1] + [digits[-1] + 1] if digits[-1] < 9 else \
            self.plusOne(digits[:-1]) + [0]
```