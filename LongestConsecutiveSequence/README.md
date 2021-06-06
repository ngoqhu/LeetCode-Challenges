## Longest Consecutive Sequence
---------
| Status | Accepted |
| --- | --- |
| Runtime | 292ms (faster than 25.35% of other python submissions) |
| Memory usage | 23.3MB (less than 26.84% of other python submissions) |
| Submissions | 918k |
| Accepted | 429.8k |
| Time Complexity | O(n . log n) |
| Space Complexity | O(1) |

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

**Example 1**
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

**Example 2**
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Constraints**
- 0 <= nums.length <= 10<sup>5</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
