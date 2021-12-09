def canJump(nums):
    goal = len(nums) - 1
    if nums == [0]:
        return True
    canSkip = False
    for i in range(len(nums)):
        if nums[i] == 0 and not canSkip:
            return False
        else:
            for j in range(1, nums[i]+1):
                if j + i == goal:
                    return True
                elif j + i < len(nums):
                    if nums[j + i] != 0:
                        canSkip = True
    return False


if __name__ == '__main__':
    arr = [3,0,8,2,0,0,1]
    print(canJump(arr))