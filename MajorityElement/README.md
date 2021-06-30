## Majority Element
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 152ms (faster than 97.88% of other python submissions) |
| Memory usage | 15.5MB (less than 79.88% of other python submissions) |
| Submissions | 1.4M |
| Accepted | 879.5k |
| Time complexity | O(n) |
| Space complexity | O(1) |

Given an array `num`s of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1**
```
Input: nums = [3,2,3]
Output: 3
```

**Example 2**
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints**
- n == nums.length
- 1 <= n <= 5 * 10<sup>4</sup>
- -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?
