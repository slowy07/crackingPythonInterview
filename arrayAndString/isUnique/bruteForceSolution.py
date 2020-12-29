def isUnique(s):
    s = s.lower()
    for c1, l1  in enumerate(s):
        for c2, l2 in enumerate(s):
            if c1 == c2:
                continue
            if l1 == l2:
                return False
    return True
