## Print In Order
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Medium |
| Runtime | 60ms (faster than 59.35% of other C# submissions) |
| Memory usage | 19.1MB |
| Submissions | 67.1k |
| Accepted | 39.6k |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

Suppose you are given the following code:

```csharp
class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
```

The same instance of `FooBar` will be passed to two different threads. Thread A will call `foo()` while thread B will call `bar()`. Modify the given program to output "foobar" *n* times.

**Example 1**
```
Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). "foobar" is being output 1 time.
```

**Example 2**
```
Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
```
