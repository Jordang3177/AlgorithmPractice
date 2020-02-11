class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return '0'
        i = len(a) - 1
        j = len(b) - 1
        holder = 1
        decA = 0
        decB = 0
        while i >= 0:
            decA = (holder * int(a[i])) + decA
            holder = holder * 2
            i = i - 1
        holder = 1
        while j >= 0:
            decB = (holder * int(b[j])) + decB
            holder = holder * 2
            j = j - 1
        answer = decA + decB
        return self.convertToBinary(answer)

    def convertToBinary(self, num: int) -> str:
        answer = ''
        while num != 0:
            if num % 2 == 0:
                answer = '0' + answer
                num = int(num//2)
            else:
                answer = '1' + answer
                num = int(num//2)
        return answer



    def testAddBinary(self):
        assert self.addBinary('11', '1') == '100'
        assert self.addBinary('1010', '1011') == '10101'
        assert self.addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101","110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011") == "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000"



if __name__ == '__main__':
    S = Solution()
    S.testAddBinary()
    print("All Tests Passed")
