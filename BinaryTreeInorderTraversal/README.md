## Binary Tree Inorder Traversal
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 48ms (faster than 6.35% of other python submissions) |
| Memory usage | 14.3MB (less than 11.11% of other python submissions) |
| Submissions | 1.3M |
| Accepted | 614.6k |
| Time Complexity | O(n) |
| Space Complexity | O(n), but average space complexity is O(log n) |

Given the root of a binary tree, return the inorder traversal of its nodes' values.

**Example 1**
```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

**Example 2**
```
Input: root = []
Output: []
```

**Example 3**
```
Input: root = [1]
Output: [1]
```


**Example 4**
```
Input: root = [1,2]
Output: [2,1]
```


**Example 5**
```
Input: root = [1,null,2]
Output: [1,2]
```

**Constraints**
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
