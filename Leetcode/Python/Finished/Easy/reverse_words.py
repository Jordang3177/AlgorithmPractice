import re

class Solution:
    def reverse_words(self, s):
        answer = ''
        holder = 0
        for m in re.finditer(' ', s):
            substring = s[holder: m.start()]
            holder = m.end()
            answer += substring[::-1] + ' '
        substring = s[holder:len(s)]
        answer += substring[::-1]
        return answer
