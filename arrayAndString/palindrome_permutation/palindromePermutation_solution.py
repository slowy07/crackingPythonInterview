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
