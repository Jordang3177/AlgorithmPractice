class Solution:
    def addToArrayForm(self, A, K):
        """
        returns the array representation of int k added to the array representation of an int A
        :param A: Array of Int
        :param K: Int
        :return: Array of Int
        """
        holder = ''
        for nums in A:
            holder += str(nums)
        holder = int(holder)
        holder += K
        holder = str(holder)
        answer = []
        for i in range(len(holder)):
            answer.append(holder[i])
        return answer