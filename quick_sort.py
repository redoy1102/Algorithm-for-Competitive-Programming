def quick_sort(nums):
    nums = list(nums)
    if len(nums) <= 1:
        return nums
    
    pivot = nums[0]
    less = [i for i in nums[1:] if i <= pivot]
    high = [i for i in nums[1:] if i > pivot]
    
    sortedNums = quick_sort(less)
    sortedNums.extend([pivot])
    sortedNums.extend(quick_sort(high))
    
    return sortedNums

print(quick_sort([1,2,3,4,5,6,0]))