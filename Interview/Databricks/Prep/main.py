from bisect import bisect_left, bisect_right, insort, insort_left
# Bisect 
# Note bisect == bisect_right (its an alias)
nums = [1, 2, 3, 3, 4]
insort_left(nums, 3) # [1, 2, 3(new), 3, 3, 4]

insort(nums, 3) # [1, 2, 3, 3, 3(new), 4]

print(nums)