# one away

## question
You are given two strings as input. You want to find out if these two strings are at most one edit away from each other.

and edit is defined as either
- inserting a character
- removing a character
- replacing a character

```
Input - "whale", "wrale"
Output - True

Input - "rake", "care"
Output - False

Input - "rake", "rake"
Output - True
```

## solution
We can first check the lengths of the two strings. If the lengths differ by more than 1, we can immediately return False since we can insert 1 character at most.

Then, we iterate through both string and compare them character by character
- if the characters are the same, continue on to the next character for both strings
- elif the characters are different and we haven't made an edit yet
  - if the lengths are the same
    - try replacing the char at string A with the char at string B
  - elif the lengths are different
    - try deleting one char from the longer string
- elif the characters are different and we have made an edit
  - return false
```python
def oneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    # p1 is pointer for s1
    # p2 is pointer for s2
    p1, p2 = 0, 0
    madeEdit = False
    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1
        elif not madeEdit:
            madeEdit = True
            if len(s1) == len(s2):
                p1 += 1
                p2 += 1
                # this represents a replacement.
                # we "pretend" there's a replacement
                # and now we can view s1[p1] as equal
                # to s2[p2] and increment p1, p2
            elif len(s1) < len(s2):
                p2 += 1
                # we "delete" the char at p2
                # and increment p2 while not
                # incrementing p1
            elif len(s1) > len(s2):
                p1 += 1
                # same as above, except for p1 now
        else:
            return False
    return True
```
