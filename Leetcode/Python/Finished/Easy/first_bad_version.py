# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        mid = n // 2
        high = n
        low = 1
        while True:
            if isBadVersion(mid) == True and isBadVersion(mid - 1) == False:
                return mid
            elif isBadVersion(mid) == False and isBadVersion(mid + 1) == True:
                return mid + 1
            elif isBadVersion(mid) == True:
                high = mid
                mid = (mid + low) // 2
            else:
                low = mid
                mid = (mid + high) // 2