class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        will return True is the student's attendance record does not contain a substring of 'LLL' or more than one 'A'
        :param s: str
        :return: bool
        """
        if s.find('LLL') != -1:
            return False
        a = s.count('A')
        if a > 1:
            return False
        return True
