def isValid(self, s):
    stack, match = [], {')': '(', ']': '[', '}': '{'}
    for character in s:
        if character in match:
            if not (stack and stack.pop() == match[character]):
                return False
         else:
             stack.append(character)
    return not stack
