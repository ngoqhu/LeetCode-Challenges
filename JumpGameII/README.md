## Jump Game II
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Medium |
| Runtime | 32ms (faster than 66.90% of other python submissions) |
| Memory usage | 14.1MB (less than 91.70% of other python submissions) |
| Submissions | 1.1M |
| Accepted | 351.6k |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

**Example 1**
```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2**
```
Input: nums = [2,3,0,1,4]
Output: 2
```

**Constraints**
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 10<sup>5</sup>
