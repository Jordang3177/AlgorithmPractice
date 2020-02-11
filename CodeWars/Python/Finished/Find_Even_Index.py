class Solution():
    def find_even_index(self, arr):
        for i in range(0, len(arr)):
            if sum(arr[0:i]) == sum(arr[i+1:len(arr)]):
                return i
        return -1

    def test_find_even_index(self):
        assert self.find_even_index([1,2,3,4,3,2,1]) == 3
        assert self.find_even_index([1,100,50,-51,1,1]) == 1
        assert self.find_even_index([20,10,-80, 10,10,15,35]) == 0
        assert self.find_even_index([10, 30]) == -1

if __name__ == "__main__":
    S = Solution()
    S.test_find_even_index()
    print("All Tests Passed")
