class Solution:
    def numJewelsInStones(self, J, S):
        """
        returns the number of things that are in J in S.
        :param J: str
        :param S: str
        :return: int
        """
        count_j = {}
        for items in J:
            count_j[items] = 0
        for items in S:
            if items in count_j:
                count_j[items] += 1
        return sum(count_j.values())