## Solutions to LeetCode Problem **Plus One** ([#66](https://leetcode.com/problems/plus-one/))

### Solution A: Pure function composition (well, the approach is somewhat cheating)

I believe it is somewhat cheating to solve the problem by heavy use of library functions for type conversion.
Anyway, the algorithm would be:

1. assemble given digits list into a number
2. increment the number by 1
3. disassemble result back into the list of digits

The above may be trivially achieved by the composition of Python 3 library functions.

Let's take, for example `digits = [1, 2, 3]`:
* `map(str, digits)` converts it to the list of strings `['1', '2', '3']`
* `''.join(map(str, digits))` further assembles it into the string `'123'`
* `int(''.join(map(str, digits)))` wrap-ups step 1 by yielding number `123`

Step 2 is just adding 1 to the above `int(''.join(map(str, digits))) + 1` that is, yielding `124`

Step 3 is continuing composing functions:
* `str(int(''.join(map(str, digits))) + 1)` converts the result number back string `'124'`
* `map(int, str(int(''.join(map(str, digits))) + 1))` converts the above into iterable over `int` digits
`map object (1, 2, 4)`
* materializing the latter with  `list(map(int, str(int(''.join(map(str, digits))) + 1)))` yields `[1, 2, 4]`,
mission accomplished!

Assembling the above into complete problem solution:
```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))
```

### Solution B: More pythonic variant of Solution A

It does not change the approach, just offers a more _pythonic_ way of implementing of Step 3 by using a list
comprehension for mapping characters of result string back into the list of `int` digits:
`[int(digit) for digit in str(int(''.join(map(str, digits))) + 1)]`. The full solution is:
```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(digit) for digit in str(int(''.join(map(str, digits))) + 1)]
```

### Solution C: Recursive function over mutating list

Now turning to the non-cheating ways of solving the problem. Intuition prompts that if the rightmost element of the
given `digits` list is less, than `9`, everything is simple: just increment this element by one and return
the (mutated) `digits`. In case of this element is `9` its value should mutate to '0' and carry-on `1` should be added
to the `digits` being shortened by one from right.
But wait a minute, this is the exact equivalent of the original problem, just the data dimension has being shrink by
one! This is where a recursive function as a solution may fit. The only question is: how the recursion stops? OK,
if the recursive function over the positions of `digits` arrives at the leftmost element and the carry-on is still
needed, this carry-on `1` must be prepended to the `digits` and recursion should stop.

The inner function `add_one` over a position of `digits` implements exactly the outlined process moving from rightmost
position until getting to a less, than `9` element value, or reaching the leftmost position, propagating the carry-on
and mutating the elements of the original `digits`.

The complete solution is given below:

```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def add_one(pos: int) -> List[int]:
            if digits[pos] < 9:
                digits[pos] += 1
                return digits
            else:
                digits[pos] = 0
                return [1] + digits if not pos else add_one(pos - 1)

        return add_one(len(digits) - 1)
```

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

What about the complexity? Apparently, it is `O(n)` for all 4 variants.