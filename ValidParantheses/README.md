## Valid Parantheses
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 32ms (faster than 57.37% of other python submissions) |
| Memory usage | 14.2MB (less than 86.97% of other python submissions) |
| Submissions | 3.5M |
| Accepted | 1.4M |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

Given a string s containing just the characters `'('`, `')'`, `'{', '}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

**Example 1**
```
Input: s = "()"
Output: true
```

**Example 2**
```
Input: s = "()[]{}"
Output: true
```

**Example 3**
```
Input: s = "(]"
Output: false
```

**Example 4**
```
Input: s = "([)]"
Output: false
```

**Example 5**
```
Input: s = "{[]}"
Output: true
```

**Constraints**
- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.
