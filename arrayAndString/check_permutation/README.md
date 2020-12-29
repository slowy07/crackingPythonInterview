# check permutation

## question
The input two strings. check if the first string is a permutation of the second string.
```
Input - "wazup bro", " orbpuwaz"
Output - True

Input - "hiiiya", "hiya"
Output - False
```
## solution
- create dictionary
- itterate through the first string
  - if the char is dictionary, increment 1 to it's value
  - if the char is not in the dictionary, set it's value to 1
After the iteration ends, we will a dictionary where the keys are the letters in the first string, and the values are the number of times that letter appears in the first string.
Now, we iterate through the second string and subtract 1 for each character from our dictionary's values. If we come across a character that's not in our dictionary we can immediately return False, since the two strings would have all the same characters if they were permutations.
- itterate through the second string
  - if the char is in the dictionary, decrement 1
  - if the char is not in the dictionary, return ``False``
- return True if the length of the dictionary is 0. That means that all the chars in the first string had an equivalent count in the second string and that the second string didn't have any extra chars that weren't in the first string.
```python
def checkPermutation(s1, s2):
    count = {}
    for i in s1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in s2:
        if i in count:
            count[i] -= 1
        else:
            return False
        if count[i] == 0:
            del count[i]
    return True
```
other solution : [brute force solution](https://github.com/slowy07/crackingPythonInterview/blob/main/arrayAndString/check_permutation/bruteForceSolution.py)
