# urlify

## question
You are given a string with spaces. You want to replace each space with ``%20``. The string will have sufficient trailing spaces at the end to contain the additional characters from the ``%20s``. You'll also be given an integer that represents the length of the string without the trailing spaces.

Strings are immutable in Python, so you'll get a character array instead (list of chars).
```
Input - ['h', 'i', ' ', 'b', 'u', 'd', ' ', ' '], 7
Output - ['h', 'i', '%', '2', '0', 'b', 'u', 'd']
```

## solution
You can solve this using the two pointer technique. One pointer (``p1``) is at the end of the array. The other pointer (``p2``) is at the end of the "true" string (it's initialized to the integer we get as input).

1. Initiate a while loop that iterates while ``p1 >= 0 and p2 >= 0``.
  - if the character at ``p2`` is not equal to " ", then copy the character at ``p2`` over to ``p1``. Decrement both pointers.
  - If the character at p2 is equal to " ", then copy over each char in ``02%`` to p1 and decrement ``p1`` as you go. Remember that we're iterating backwards, which is why we use ``02%`` instead of ``%20``. Then, decrement both pointers
2. Exit the function
```python
def urlify(s, i):
    p1, p2 = len(s) - 1, i
    while p1 >= 0 and p2 >= 0:
        if s[p2] != " ":
            s[p1] = s[p2]
        else:
            for i in reversed("%20"):
                s[p1] = i
                p1 -= 1
        p1 -= 1
        p2 -= 1
```
