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
