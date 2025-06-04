def searchInsert(nums, target):
    if len(nums) > 0:
        index = 0
        for i in nums:
            if target == i:
                break
            elif target > i:
                index += 1
            else:
                break
        return index
    else:
        return 0

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    print(searchInsert(nums, target))