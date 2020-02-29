class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if n == 0:
                return True
            elif i == 0:
                if flowerbed[i] != 1 and flowerbed[i + 1] != 1:
                    flowerbed[i] = 1
                    i += 2
                    n -= 1
                else:
                    i += 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] != 1 and flowerbed[i - 1] != 1:
                    flowerbed[i] = 1
                    i += 1
                    n -= 1
                else:
                    i += 1
            else:
                if flowerbed[i] != 1 and flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1:
                    flowerbed[i] = 1
                    i += 2
                    n -= 1
                else:
                    i += 1
        return n == 0


S = Solution()
print(S.canPlaceFlowers([1,0,0,0,1,0,0], 2))