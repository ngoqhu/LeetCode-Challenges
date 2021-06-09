## Same Tree
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 44ms (faster than 8.16% of other python submissions) |
| Memory usage | 14.2MB (less than 84.68% of other python submissions) |
| Submissions | 1.4M |
| Accepted | 737.8k |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example 1**
```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2**
```
Input: p = [1,2], q = [1,null,2]
Output: false
```

**Example 3**
```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

**Constraints**
- The number of nodes in both trees is in the range [0, 100].
- -10<sup>4</sup> <= Node.val <= 10<sup>4</sup>
