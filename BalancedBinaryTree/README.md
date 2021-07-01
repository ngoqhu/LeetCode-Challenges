## Balanced Binary Tree
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 52ms (faster than 65.75% of other python submissions) |
| Memory usage | 19.4MB (less than 6.70% of other python submissions) |
| Submissions | 1.3M |
| Accepted | 592.3 |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
> a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

**Example 1**

<img src=https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg>

```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2**

<img src=https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg>

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3**
```
Input: root = []
Output: true
```

**Constraints**
- he number of nodes in the tree is in the range [0, 5000].
- -10<sup>4</sup> <= Node.val <= 10<sup>4</sup>
