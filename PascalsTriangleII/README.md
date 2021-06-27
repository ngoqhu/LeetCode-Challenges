## Pascal's Triangle II
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 32ms (faster than 62.89% of other python submissions) |
| Memory usage | 13.9MB (less than 99.92% of other python submissions) |
| Submissions | 721.2k |
| Accepted | 338.6k |
| Time Complexity | O(n) |
| Space Complexity | O(n<sup>2</sup>/2 |

Given an integer rowIndex, return the rowIndex<sup>th</sup> (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

<img src=https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif>

**Example 1**
```
Input: rowIndex = 3
Output: [1,3,3,1]
```

**Example 2**
```
Input: rowIndex = 0
Output: [1]
```

**Example 3**
```
Input: rowIndex = 1
Output: [1,1]
```

**Constraints**
- 0 <= rowIndex <= 33

**Follow up:** Could you optimize your algorithm to use only `O(rowIndex)` extra space?
