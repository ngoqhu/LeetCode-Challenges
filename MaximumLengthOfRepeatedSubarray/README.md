## Maximum Length of Repeated Subarray
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Medium |
| Runtime | 6780ms (faster than 6.58% of other python submissions) |
| Memory usage | 40.2MB (less than 20.54% of other python submissions) |
| Time Complexity | O(m . n), where `m` and `n` are sizes of arrays `nums1` and `nums2` |
| Space Complexity | O(m . n), where `m` and `n` are sizes of arrays `nums1` and `nums2` |
| Submissions | 223.9k |
| Accepted | 114.7k |

Given two integer arrays `nums1` and `nums2`, return *the maximum length of a subarray that appears in **both** arrays*.

**Example 1**
```
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
```

**Example 2**
```
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
```

**Constraints**
- 1 <= `nums1.length`, `nums2.length` <= 1000
- 0 <= `nums1[i]`, `nums2[i]` <= 100
