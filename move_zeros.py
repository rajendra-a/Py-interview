def move_zeros(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums


print(move_zeros([0, 1, 0, 1, 12]))