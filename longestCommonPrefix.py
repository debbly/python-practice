def longestCommonPrefix(self, strings):
    count = len(strings)
    
    if count == 0:
        return ""
    
    minstring = min(strings)
    length = len(minstring)

    while length > 0:
        found = True
        substring = minstring[:length]
        for i in range(count):
            if not strings[i].startswith(substring):
                found = False
                break
        if found:
            break
        length -= 1

    return minstring[:length]
