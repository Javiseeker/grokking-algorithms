def findMaxNumber(biggest, nums):
    if len(nums) == 0:
        return biggest
    if nums[-1] > biggest:
        biggest = nums[-1]
    nums.pop()
    return findMaxNumber(biggest, nums)

nums = [5,3,2,7,1, 10]
neg_inf = float('-inf')
result = findMaxNumber(neg_inf, nums)
print(f"result: {result}")