def excelCol(self, s):
    key = 0
    length = len(s)
    count = 0
    if not s:
        return s
    else:
        for i in s:
            key += (ord(i) - 64)*pow(26, l - 1 - count)
            count += 1
        return key
