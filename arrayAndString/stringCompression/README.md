# string compression

## question
You are given a string that may or may not contain repeated characters. Write a function that "compresses" the string so that repeated characters that are next to each other are replaced by the character and the count. If the length of the compression is longer than the length of the original string, return the original string.
```python
Input - aaaabbccd
Output - a4b2c2d1

Input - aabcd
Output - aabcd
```

## solution
We can solve this problem by iterating through the string and counting the occurrences of each letter. As we count the occurences, we keep a separate array where we append the letter and the number of times it occurs. At the end, we can just convert that array to a string and return either the compressed array or the original string (whichever one is shorter).
- Remember that strings are immutable in Python, so when we're building the compressed string, we must do so with a list. After building the compressed string, we can then convert it to a string.
```python
def stringCompression(s):
    compressedString = []
    cur = s[0]
    counter = 1
    for l in s[1:]:
        if l == cur:
            counter += 1
        else:
            compressedString.append(cur)
            compressedString.append(str(counter))
            cur = l
            counter = 1
    compressedString.append(cur)
    compressedString.append(str(counter))
    compressedString = "".join(compressedString)

    if len(compressedString) < len(s):
        return compressedString
    else:
        return s
```
