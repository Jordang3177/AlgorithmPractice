# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head) -> int:
        answer = self.getValuesFromList(head)
        binaryString = ''.join(answer)
        integerOfBinary = self.toBinary(binaryString)
        return integerOfBinary

    def getValuesFromList(self, head):
        valuesArray = []
        while head:
            valuesArray.append(str(head.val))
            head = head.next
        return valuesArray

    def toBinary(self, s):
        intOfS = 0
        reverseS = s[::-1]
        power = 0
        for i in range(len(reverseS)):
            intOfS += 2 ** power * int(reverseS[i])
            power += 1
        return intOfS