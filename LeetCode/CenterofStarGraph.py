def findCenter(edges):
    result = set(edges[0])
    for s in edges[1:]:
        result.intersection_update(s)
    return result.pop()


if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [4, 2]]
    print(findCenter(edges))
