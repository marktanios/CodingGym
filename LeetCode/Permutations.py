def cal_permute(rootNode, remaningList):
    if rootNode == None:
        childNodes = remaningList
        result = []
    if len(remaningList) == 1:
        return remaningList

    for item in remaningList:
        n = remaningList.pop(0)
        l = cal_permute(n, remaningList)
        l.append(n)


def permute(nums):
    if len(nums) == 1:
        return [nums]
    else:
        cal_permute(None, nums)
