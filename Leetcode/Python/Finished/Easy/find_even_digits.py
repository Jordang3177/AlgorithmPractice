class Solution:
    def findNumbers(self, nums):
        """
        
        :param nums:
        :return:
        """
        answer = 0
        for number in nums:
            if len(str(number)) % 2 == 0:
                answer += 1
        return answer