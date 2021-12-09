def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    Answer = []
    for i in range(len(s)):
        #check odd Palindromic Substrings
        left = i
        right = i
        while s[right] == s[left] and left >=0 and right < len(s):
            Answer.append(s[left:right+1])
            right += 1
            left -= 1
            if left < 0 or right >= len(s):
                break
        #check even Palindromic Substrings
        left = i
        if i < len(s)-1:
            right = i + 1
        else:
            return len(Answer)
        while s[right] == s[left] and left >=0 and right < len(s):
            Answer.append(s[left:right+1])
            right += 1
            left -= 1
            if left < 0 or right >= len(s):
                break


if __name__ == '__main__':
    StringText = 'abc'
    print(countSubstrings(StringText))