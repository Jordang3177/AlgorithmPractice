class Solution:
    def smallerNumbersThanCurrent(self, nums):
        """
        returns an array of how many values are smaller than each value in the given array
        :param nums: Array of Int
        :return: Array of Int
        """
        dictionary_counter = {}
        answer = []
        sort_nums = sorted(nums)
        for i in range(len(nums)):
            if sort_nums[i] not in dictionary_counter:
                dictionary_counter[sort_nums[i]] = i
        return [dictionary_counter[num] for num in nums]