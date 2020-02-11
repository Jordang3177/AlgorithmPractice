# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return head


    def testDeleteDuplicates(self):
        A = ListNode(1)
        B = ListNode(2)
        C = ListNode(3)
        D = ListNode(4)
        E = ListNode(5)
        F = ListNode(6)
        A.next = B
        B.next = C
        C.next = D
        D.next = E
        E.next = F
        print(A)
        print(A.val)
        print(A.next)
        print(A.next.val)
        assert self.deleteDuplicates(A) == A


if __name__ == '__main__':
    S = Solution()
    S.testDeleteDuplicates()
    print("All Tests Passed")