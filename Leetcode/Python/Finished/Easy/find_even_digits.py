class Solution:
    def findNumbers(self, nums):
        """
        returns the number of numbers in the list with even digits
        :param nums: Array of Int
        :return: int
        """
        answer = 0
        for number in nums:
            if len(str(number)) % 2 == 0:
                answer += 1
        return answer