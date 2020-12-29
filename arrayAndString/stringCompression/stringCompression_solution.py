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
