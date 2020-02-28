class Solution:
    def decompressRLElist(self, nums):
        """
        the even indexs are the frequency for the odd indexs to be returned in a list
        :param nums: Array of Int
        :return: Array of Int
        """
        answer = []
        while nums:
            for i in range(nums[0]):
                answer.append(nums[1])
            nums.pop(0)
            nums.pop(0)
        return answer