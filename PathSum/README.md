## Path Sum
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 44ms (faster than 59.22% of other python submissions) |
| Memory usage | 15.9MB (less than 69.49% of other python submissions) |
| Submissions | 1.5M |
| Accepted | 633.2k |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

**Example 1**
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
```

**Example 2**
```
Input: root = [1,2,3], targetSum = 5
Output: false
```

**Example 3**
```
Input: root = [1,2], targetSum = 0
Output: false
```

**Example 4**
```
Input: root = [0]
Output: 1
```

**Constraints**
- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000