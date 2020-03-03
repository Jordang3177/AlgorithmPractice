class Solution(object):
    def isValid(self, s):
        """
        returns if the given string has a valid opening and closing property of brackets, parenthesis, and curly brackets
        :param s: string
        :return: boolean
        """
        stack = []
        ending_values = {')': '(', ']': '[', '}':'{'}
        for char in s:
            if char in ending_values:
                if stack:
                    popped_value = stack.pop()
                else:
                    popped_value = '%'
                if ending_values[char] != popped_value:
                    return False
            else:
                stack.append(char)
        if len(stack) > 0:
            return False
        else:
            return True
