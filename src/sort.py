def binary_search(nums, ele):
    # Supposing that nums are sorted ascent to find lower_bound of nums
    left = -1
    right = len(nums)
    while left + 1 < right:
        mid = left + (right - left) // 2
        if ele <= nums[mid]:
            right = mid
        else:
            left = mid
    return right


def selection_sort(nums):
    for i in range(len(nums)):
        mn = 1000000000000
        mn_i = -1
        for j in range(i, len(nums)):
            if nums[j] < mn:
                mn = nums[j]
                mn_i = j
        nums[i], nums[mn_i] = nums[mn_i], nums[i]
    return nums


def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1, i, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums


def insertion_sort(nums):
    for i in range(1, len(nums)):
        idx = binary_search(nums[:i], nums[i])
        nums[:] = nums[:idx] + [nums[i]] + nums[idx:i] + nums[i + 1:]
    return nums


def merge_sort(nums):
    def merge(left, right):
        li = 0
        ri = 0
        merged = []
        while li < len(left) and ri < len(right):
            if left[li] < right[ri]:
                merged.append(left[li])
                li += 1
            else:
                merged.append(right[ri])
                ri += 1
        if li < len(left):
            merged += left[li:]
        elif ri < len(right):
            merged += right[ri:]
        return merged
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def quick_sort(nums):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    left = []
    right = []
    for i in range(1, len(nums)):
        if nums[i] <= pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
