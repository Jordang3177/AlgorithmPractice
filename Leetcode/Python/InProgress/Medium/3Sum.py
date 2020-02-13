class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        i = 0
        j = 1
        answer = []
        while i != len(nums):
            while j != len(nums):
                if i == j:
                    j += 1
                    continue
                remainder = nums[i] + nums[j]
                find = 0 - remainder
                lessnums = nums[0:i] + nums[i + 1:j] + nums[j + 1:len(nums)]
                if lessnums.__contains__(find):
                    k = nums.index(find)
                    holder = [nums[i], nums[j], nums[k]]
                    holder.sort()
                    if holder in answer:
                        j += 1
                        continue
                    answer.append(holder)
                j += 1
            i += 1
            j = i + 1
        return answer

    def testThreeSum(self):
        assert self.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1],[-1,-1,2]]


if __name__ == '__main__':
    S = Solution()
    S.testThreeSum()
    print("All Tests Passed")
