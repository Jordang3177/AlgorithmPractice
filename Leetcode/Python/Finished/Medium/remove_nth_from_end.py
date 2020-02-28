class Solution:
    def removeNthFromEnd(self, head, n):
        """
        removes the nth from the end element and returns the new corresponding linked list
        :param head: linked list
        :param n: int
        :return: linked list
        """
        dummy = head
        length = 0
        while dummy is not None:
            length += 1
            dummy = dummy.next
        if length == n:
            return head.next
        dummy = head
        nth_element_to_remove = length - n
        while nth_element_to_remove != 1:
            dummy = dummy.next
            nth_element_to_remove -= 1
        if n == 0:
            dummy.next = None
            return head
        dummy.next = dummy.next.next
        return head