def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    #l == '(' or l == '{' or l == '[':
    validList = []
    for l in s:
        if len(validList) == 0:
            validList.append(l)
        else:
            if l == ')' and validList[-1] == '(':
                del validList[-1]
            elif l == '}' and validList[-1] == '{':
                del validList[-1]
            elif l == ']' and validList[-1] == '[':
                del validList[-1]
            else:
                validList.append(l)
    if len(validList) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    testString = '{[]}'
    print(isValid(testString))
