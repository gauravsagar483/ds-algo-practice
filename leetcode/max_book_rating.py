nums = [-1, -3, -2]


def max_rating(nums, index, prev, sum=0):

    if index >= len(nums):

        return 0

    # sum += nums[index]

    if nums[index] > 0:
        return nums[index] + max_rating(nums, index + 1, index, sum)
    else:
        print(
            index,
            nums[index] + max_rating(nums, index + 2, index, sum),
            max_rating(nums, index + 1, index, sum),
        )

        return max(
            nums[index] + max_rating(nums, index + 2, index, sum),
            max_rating(nums, index + 1, index, sum),
        )


print(max_rating(nums, 0, 0))
