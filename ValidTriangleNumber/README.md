## Valid Triangle Number
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Medium |
| Runtime | 996ms (faster than 99.74% of other python submissions) |
| Memory usage | 14.24B (less than 3.49% of other python submissions) |
| Time Complexity | O(n) |
| Space Complexity | O(1) |
| Submissions | 209.9k |
| Accepted | 103.6k |

Given an integer array `nums`, return *the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle*.


**Example 1**
```
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
```

**Example 2**
```
Input: nums = [4,2,3,4]
Output: 4
```

**Constraints**
- 1 <= `nums.length` <= 1000
- 0 <= `nums[i]` <= 1000
