# Loop detection

## question
You are given a linked list as input. The linked list may or may not have a cycle. Write a function that returns the node at the beginning of the cycle (if it exists) or None.
```
Input - 1 -> 2 -> 3 -> 4 -> 2 (same 2 as earlier)
Output - 2
```

## solution
The fastest we can do is $$O(n)$$ time complexity. But can we improve space complexity?
We can! We can solve this in constant space using Floyd's Cycle Detection Algorithm. This algorithm is pretty simple to understand, but it's best if done with a video. Therefore, we'll let Gayle explain it herself!.
```python
def intersection(head):
    slow, fast = head.next, head.next.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
```
