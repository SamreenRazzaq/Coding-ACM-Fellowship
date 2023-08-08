#Remove duplicates from sorted array

def removeDuplicates(nums):
    if not nums:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

# Example usage
sorted_array = [1, 1, 2, 2, 3, 4, 4, 4, 5]
new_length = removeDuplicates(sorted_array)
print("New length:", new_length)
print("Updated array:", sorted_array[:new_length])
