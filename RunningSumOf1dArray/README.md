## Maximum Points You Can Obtain from Cards
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 40ms (faster than 64.80% of other python submissions) |
| Memory usage | 14.4MB (less than 39.15% of other python submissions) |
| Submissions | 428.2k |
| Accepted | 380.4k |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of `nums`.

**Example 1**
```
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

**Example 2**
```
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
```

**Example 3**
```
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

**Constraints**
- 1 <= nums.length <= 1000
- -10<sup>6</sup> <= nums[i] <= 10<sup>6</sup>
