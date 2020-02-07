def twoSum(self, nums, target):
    index = 0
    seen = {}
    for num1 in nums:
        remaining = target - num1
        if remaining in seen:
            return [seen[remaining], index]
        seen[num1] = index
        index += 1