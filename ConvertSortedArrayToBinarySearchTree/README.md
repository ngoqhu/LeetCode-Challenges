## Convert Sorted Array to Binary Search Tree
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 64ms (faster than 38.24% of other python submissions) |
| Memory usage | 15.7MB (less than 58.59% of other python submissions) |
| Submissions | 897.4k |
| Accepted | 556.5k |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

Given an integer array `nums` where the elements are sorted in **ascending order**, convert it to a **height-balanced** binary search tree.

A **height-balanced** binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

**Example 1**

<img src=https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg>

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
```

<img src=https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg>

**Example 2**

<img src=https://assets.leetcode.com/uploads/2021/02/18/btree.jpg>

```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
```

**Constraints**
- 1 <= `nums.length` <= 10<sup>4</sup>
- -10<sup>4</sup> <= `nums[i]` <= 10<sup>4</sup>
- `nums` is sorted in a strictly increasing order.
