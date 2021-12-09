def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    myList = []
    for i in nums:
        if i in myList:
            myList.remove(i)
        else:
            myList.append(i)
    return myList[0]


if __name__ == '__main__':
    print(singleNumber([0,1,0,1,0,1,99]))