def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums or len(nums)==0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0],nums[1])
    nums.append(nums[0])
    dp = [nums[0], max(nums[0], nums[1])]

    for i in range(2, len(nums)):
        dp.append(max(nums[i]+nums[i-2], dp[i-1]))
    return dp[len(nums)-1]


if __name__ == '__main__':
    print(rob([2,3,1]))
