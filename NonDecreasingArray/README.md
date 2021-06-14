## Non-Decresing Array
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Medium |
| Runtime | 172ms (faster than 96.17% of other python submissions) |
| Memory usage | 15.4MB (less than 56.93% of other python submissions) |
| Submissions | 731.2k |
| Accepted | 152.6k |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

Given an array `nums` with `n` integers, your task is to check if it could become non-decreasing by modifying **at most one element**.

We define an array is non-decreasing if `nums[i] <= nums[i + 1]` holds for every `i` **(0-based)** such that `(0 <= i <= n - 2)`.

**Example 1**
```
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
```

**Example 2**
```
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
```

**Constraints**
- n == nums.length
- 1 <= n <= 10<sup>4</sup>
- -10</sup>5</sup> <= nums[i] <= 10<sup>5</sup>
