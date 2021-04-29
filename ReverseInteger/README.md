## Reverse Integer
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 28ms (faster than 86.66% of other python submissions) |
| Memory usage | 13.9MB (less than 98.48% of other python submissions) |
| Submissions | 5.8M |
| Accepted | 1.5M |
| Time Complexity | O(log(n)) |
| Space Complexity | O(1) |

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2<sup>31</sup>, 2<sup>31</sup> - 1], then return 0.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

**Example 1**
```
Input: x = 123
Output: 321
```

**Example 2**
```
Input: x = -123
Output: -321
```

**Example 3**
```
Input: x = 120
Output: 21
```

**Example 4**
```
Input: x = 0
Output: 0
```

**Constraints**
- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1
