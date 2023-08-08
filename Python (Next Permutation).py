#Next Permutation:

def nextPermutation(nums):
    # Find the first decreasing element from the right
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # If no decreasing element found, reverse the entire list
    if i == -1:
        nums.reverse()
        return

    # Find the smallest element greater than nums[i] from the right
    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1

    # Swap nums[i] and nums[j]
    nums[i], nums[j] = nums[j], nums[i]

    # Reverse the subarray after index i to get the next permutation
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Example usage
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
