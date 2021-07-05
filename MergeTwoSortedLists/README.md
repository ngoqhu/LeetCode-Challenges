## Merge Two Sorted Lists
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 28ms (faster than 98.01% of other python submissions) |
| Memory usage | 14.4MB (less than 7.21% of other python submissions) |
| Submissions | 2.6M |
| Accepted | 1.5M |
| Time Complexity | O(n . m), where `m` is length of first list and `l` is complexity of second list |
| Space Complexity | O(1) |

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

**Example 1**

<img src=https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg>

```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2**
```
Input: l1 = [], l2 = []
Output: []
```

**Example 3**
```
Input: l1 = [], l2 = [0]
Output: [0]
```

**Constraints**
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both l1 and l2 are sorted in **non-decreasing** order.
