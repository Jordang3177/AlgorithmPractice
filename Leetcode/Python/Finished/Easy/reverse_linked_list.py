# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        returns the reverse of the given Linked List
        :param head: ListNode
        :return: ListNode
        """
        reversed_order = []
        while head != None:
            reversed_order.insert(0, head.val)
            head = head.next
        reversed_linked_list = ListNode(0)
        holder = reversed_linked_list
        while reversed_order:
            holder.next = ListNode(reversed_order.pop(0))
            holder = holder.next
        return reversed_linked_list.next