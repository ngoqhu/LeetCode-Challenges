## Search Insert Position
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 44ms (faster than 89.21% of other python submissions) |
| Memory usage | 15.1MB (less than 52.13% of other python submissions) |
| Submissions | 1.9M |
| Accepted | 900k |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

**Example 1**
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2**
```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3**
```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

**Example 4**
```
Input: nums = [1,3,5,6], target = 0
Output: 0
```

**Example 5**
```
Input: nums = [1], target = 0
Output: 0
```

**Constraints**
- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- nums contains distinct values sorted in ascending order.
- -10<sup>4</sup> <= target <= 10<sup>4</sup>
