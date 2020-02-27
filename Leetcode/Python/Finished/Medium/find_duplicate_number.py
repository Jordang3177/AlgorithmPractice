class Solution:
    def findDuplicate(self, nums) -> int:
        slow_pointer = 0
        fast_pointer = 0

        slow_pointer = nums[slow_pointer]
        fast_pointer = nums[nums[fast_pointer]]

        while slow_pointer != fast_pointer:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]

        a_pointer = 0
        b_pointer = slow_pointer

        while a_pointer != b_pointer:
            a_pointer = nums[a_pointer]
            b_pointer = nums[b_pointer]
        return a_pointer

S = Solution()
S.findDuplicate([1,3,4,2,2])