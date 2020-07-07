## Solutions to LeetCode Problem **Plus One** ([#66](https://leetcode.com/problems/plus-one/))

### Solution A: Pure function composition (well, the approach is cheating)

### Solution B: More pythonic variant of Solution A

### Solution C: Recursive function over mutating list

### Solution D: Genuine Divide-and-Conquer Approach

* Apparently if the last element of `digits` is less, than `9`, the solution is just the input list having the last element incremented by one, that is,  `digits[:-1] + [digits[-1] + 1]`.

* If the last element of `digits` equals `9` the solution of the original problem is the solution for the `digits` shortened by throwing out the last element, or `self.plusOne(digits[:-1])`;  appended by `0`,
or `self.plusOne(digits[:-1]) + [0]`. Why is that? Because `9 + 1` gives `10`, of which `1` goes as carry-on **plus-one** to the shortened list and `0` substitutes the place occupied by `9`.

* Finally, what if original list of digits by subsequent decreasing in size gets empty? In this case we just need to return leftover carry-on [1].

Putting all the above together gives an elegant one-statement solution:
```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [1] if not digits else \
            digits[:-1] + [digits[-1] + 1] if digits[-1] < 9 else \
            self.plusOne(digits[:-1]) + [0]
```