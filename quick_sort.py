def quick_sort(nums):
    nums = list(nums)
    if len(nums) < 1:
        return nums
    
    pivot = nums[0]
    less = [i for i in nums[1:] if i <= pivot]
    high = [i for i in nums[1:] if i > pivot]
    
    sortedNums = quick_sort(less)
    sortedNums.extend([pivot])
    sortedNums.extend(quick_sort(high))
    
    return sortedNums


nums = [i for i in input("Enter a sequence: ").split()]
print("Sorted sequence:", quick_sort(nums))