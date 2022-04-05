# Monotonic means if and only if it is monotone increasing or monotone decreasing in order to assess it
def monotonic_array(nums):
    return (all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) 
            or all(nums[i] >= nums[i+1] for i in range(len(nums)-1)))

print(monotonic_array([6, 5, 4,4]))