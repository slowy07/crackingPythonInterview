# Delete Middle Node

## question
You're given a pointer to a node in a singly linked list. The node will NOT be the last node in the singly linked list. Write a function that deletes only that node in the linked list in-place. You don't have to return anything since the deletion is in-place.
```
Linked List - 1 -> 2 -> 3 -> 4 -> 5 -> 3
Input - 4 -> 5 -> 3
Result after running function - 1 -> 2-> 3 -> 5 -> 3
```

## solution
We need to modify the original linked list and delete the node that the pointer is pointing at. We can't delete the node because we don't have a pointer to the previous node (check hint). Therefore, we can mimic a deletion by copying over the value from the next node into the node we want to delete. Then, we can just delete the next node in the standard fashion.
```python
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
```
