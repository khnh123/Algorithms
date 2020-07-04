import numpy as np

nums = list(np.random.randint(low=1, high=100, size=10)) # generate list
print(nums)

# Bubble Sort
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]: # swap until elem is larger tha elem + 1
                nums[j], nums[j+1] = nums[j+1], nums[j]


def bubble_sort_2(nums):
    # changes the list - no need to return anything
    swaps = True
    while swaps: # while swaps exist
        swaps = False
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                swaps = True  # swap until elem is larger tha elem + 1
            nums[j], nums[j+1] = nums[j+1],  nums[j]
