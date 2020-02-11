def removeDuplicates(nums):
    newlist = []
    for i in range(len(nums)):
        if nums[i] in newlist:
            pass
        else:
            newlist.append(nums[i])
    nums = newlist
    return len(nums)

print(removeDuplicates([1,2,3,4]))
print(removeDuplicates([1,1,1,1,1,1,1]))
print(removeDuplicates([1,1,2]))

a = set()
a = a.union(valuesinRows[i])