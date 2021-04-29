## Palindrome Number
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 72ms (faster than 24.26% of other python submissions) |
| Memory usage | 14.1MB (less than 92.31% of other python submissions) |
| Submissions | 2.5M |
| Accepted | 1.2M |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

Given an integer `x`, return `true` if `x` is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward. For example, `121` is palindrome while `123` is not.

**Example 1**
```
Input: x = 121
Output: true
```

**Example 2**
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3**
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Constraints**
- -231 <= x <= 231 - 1
