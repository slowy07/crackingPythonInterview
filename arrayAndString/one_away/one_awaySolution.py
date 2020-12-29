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
