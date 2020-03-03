class Solution:
    def containsDuplicate(self, nums):
        """
        returns if the given nums contains a duplicate number
        :param nums: Array of int
        :return: boolean
        """
        holder = set()
        for i in range(len(nums)):
            if nums[i] in holder:
                return True
            else:
                holder.add(nums[i])
        return False
