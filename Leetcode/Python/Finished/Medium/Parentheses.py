class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return ['']
        left, right, ans = n, n, []
        self.dfs(left, right, ans, '')
        return ans

    def dfs(self, l, r, ans, string):
        if r < l:
            return
        if l == 0 and r == 0:
            ans.append(string)
            return
        if l:
            self.dfs(l-1, r, ans, string +'(')
        if r:
            self.dfs(l, r-1, ans, string + ')')

    def testGenerateParenthesis(self):
        assert self.generateParenthesis(0) == ['']
        assert self.generateParenthesis(1) == ['()']
        assert self.generateParenthesis(2) == ['(())', '()()']
        assert self.generateParenthesis(4) == ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
        assert self.generateParenthesis(5) == ["((((()))))","(((()())))","(((())()))","(((()))())","(((())))()","((()(())))","((()()()))","((()())())","((()()))()","((())(()))","((())()())","((())())()","((()))(())","((()))()()","(()((())))","(()(()()))","(()(())())","(()(()))()","(()()(()))","(()()()())","(()()())()","(()())(())","(()())()()","(())((()))","(())(()())","(())(())()","(())()(())","(())()()()","()(((())))","()((()()))","()((())())","()((()))()","()(()(()))","()(()()())","()(()())()","()(())(())","()(())()()","()()((()))","()()(()())","()()(())()","()()()(())","()()()()()"]




if __name__ == "__main__":
    S = Solution()
    S.testGenerateParenthesis()
    print("All Tests Passed")
