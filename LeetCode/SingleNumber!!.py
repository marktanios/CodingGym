def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    myList = []
    removedList = []
    for i in nums:
        if i in myList:
            myList.remove(i)
            removedList.append(i)
        else:
            myList.append(i)
    return list(set(myList) - set(removedList))[0]


if __name__ == '__main__':
    print(singleNumber([0,1,0,1,0,1,99]))