def modified_binary_search(nums, target: int) -> int:

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        if nums[low] <= nums[mid]:
            low, high = (
                (low, mid - 1) if nums[low] <= target < nums[mid] else (mid + 1, high)
            )
        else:
            low, high = (
                (mid + 1, high) if nums[low] > target >= nums[mid] else (low, mid - 1)
            )

    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(modified_binary_search(nums, target))
