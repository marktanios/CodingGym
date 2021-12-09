def findJudge(n, trust):
    """
    :type n: int
    :type trust: List[List[int]]
    :rtype: int
    """
    trustees = set()
    for i in trust:
        if i[1] not in trustees:
            trustees.add(i[1])
    for i in trust:
        if i[0] in trustees:
            trustees.remove(i[0])
    if len(trustees) == 1:
        return trustees.pop()
    else:
        return -1


if __name__ == '__main__':
    n = 2
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    out = findJudge(n, trust)
    print(out)