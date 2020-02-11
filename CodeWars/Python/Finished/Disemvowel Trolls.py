class Solution():
    def disemvowel(self, string):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        answer = ''
        for values in string:
            if values in vowels:
                continue
            else:
                answer += values
        return answer

    def test_disemvowel(self):
        assert self.disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"
        assert self.disemvowel("o") == ''
        assert self.disemvowel('hello there') == 'hll thr'

if __name__ == '__main__':
    S = Solution()
    S.test_disemvowel()
    print("All Tests Passed")
