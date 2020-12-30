# Intersection

## question
You are given two singly linked lists. Write a function to determine if the two lists intersect. If they do intersect, return the node at which the two lists intersect. Otherwise, return None.
```
Input -
1 -> 2 -> 3 ->
               4 -> 5 -> 6
          2 ->

Output - 4 -> 5 -> 6
(the output is the node with the value 4)
```

## solution
We will use two pointers, ``p1`` and ``p2``. ``p1`` points to the head of ``l1`` and ``p2`` points to the head of ``l2``. We'll traverse both linked lists. When ``p1`` reaches the tail of ``l1``, then we will redirect ``p1`` to the head of ``l2``. We do the same for ``p2``. When p2 reaches the tail of ``l2``, we will redirect it to l1. If the pointers are ever pointing to the same node (``p1 == p2``), then that is the intersecting node. Let's talk about why this approach works.
```python
def intersection(l1, l2):
    p1 = l1
    p2 = l2
    p1Switch = False
    p2Switch = False

    while (p1 or not p1Switch) and (p2 or not p2Switch):
        if p1 == p2:
            return p1
        p1 = p1.next
        p2 = p2.next

        if p1 is None and not p1Switch:
            p1 = l2
            p1Switch = True

        if p2 is None and not p2Switch:
            p2 = l1
            p2Switch = True
```
