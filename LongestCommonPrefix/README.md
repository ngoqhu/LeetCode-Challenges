## Longest Common Prefix
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 48ms (faster than 5.78% of other python submissions) |
| Memory usage | 14.3MB (less than 82.3% of other python submissions) |
| Submissions | 2.8M |
| Accepted | 1M |
| Time Complexity | O(n.L), L is length of longest string |
| Space Complexity | O(1) |

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1**
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2**
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Constraints**
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lower-case English letters.
