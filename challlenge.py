def twosum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        new_num = target - num 
        if new_num in seen:

            return seen[new_num], i
        seen[num]=i
    return "Number not available"


nums = [
    1, 4, 5, 9, 40, 9, 17, 90, 2
]
target = 80
print(twosum(nums, target))