def lengthOfLastWord(self, s):
    if not s or len(s.strip()) < 1:
        return 0
    l = s.strip().split()
    return len(l[len(l) - 1])
