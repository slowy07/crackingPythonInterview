# is unique

## question
You are given a string. Write a function to determine if all of the characters in the string appear only once.
Your function shouldn't care about capitalization. A is the same as a.

```
Input - "heLlo"
Output - False

Input - "hey"
Output - True
```

## solution

instead of using two loops,we can use set.as we iterate through the string, we check if the current letter is the set.
if it is, then we return ``false`` otherwise,we add the current letter to the set and continue iterating
```python
def isUnique(s):
    s = s.lower()
    seen = set()
    for i in s:
      if i in seen:
          return False
    return True
```
other solution : [brute force solution](https://github.com/slowy07/crackingPythonInterview/blob/main/arrayAndString/isUnique/bruteForceSolution.py)
