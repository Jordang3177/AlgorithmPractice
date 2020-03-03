class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        """
        returns if there is a duplicate number in nums and they are a max distance of k from each other
        :param nums: Array of Int
        :param k: int
        :return: boolean
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict and abs(dict[nums[i]] - i) <= k:
                return True
            else:
                dict[nums[i]] = i
        return False