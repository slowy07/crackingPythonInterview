# palindrome permutation

## question
You are given a string. Write a function that checks if the letters in the string can be rearranged to form a palindrome (or if the input is already a palindrome). You can ignore spaces in the string.
```
Input - "car race"
Output - True (the letters can be rearranged to " racecar")
```

## solution
In order to solve this, we need to think about the properties of a palindrome. You should write a couple of palindromes down and see if you can notice any patterns. they either
- have an even number of characters. Ex. ``caac`` a - 2, c - 2
- have an odd number of characters, where there's only one character that appears an odd number of times. Ex. ``cabbbac`` a - 2, b - 3, c - 2
In other words, a palindrome is a string that can be reversed to produce the same string. That means that either every character has a matching pair, or there is only one character that appears an odd number of times (and that character will be placed in the middle of the string for the palindrome).
We can count the number of occurrences of each character with a dictionary.
```python
def checkPermutation(s):
    counts = {}
    for i in s:
        if i == " ":
            continue
        if i in counts.items():
            counts[i] += 1
        else:
            counts[i] = 1
    hasOdd = False
    for key, value in counts:
        if value % 2 == 1:
            if hasOdd:
                # we have more than one char
                # that appears an odd number
                # of times
                return False
            hasOdd = True

    return True
```
