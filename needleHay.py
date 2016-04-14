def needleHay(self, haystack, needle):
    haystackRef, haystackSize, needleSize = 0, len(haystack), len(needle)
    while True:
        needleRef = 0
        while True:
            if needleSize == needleRef: return haystackRef
            if haystackRef + needleSize == haystackSize: return -1
            if needle[needleRef] != haystack[haystackRed + needleRef]: break
            needleRef += 1
        haystackRef += 1
