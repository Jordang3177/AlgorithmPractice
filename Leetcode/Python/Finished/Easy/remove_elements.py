# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        Removes all vals in the LinkedList and returns the new LinkedList
        :param head: ListNode
        :param val: int
        :return: ListNode
        """
        extra = ListNode(1)
        extra.next = head
        holder = extra
        while holder != None and holder.next != None:
            if holder.next.val == val:
                holder.next = holder.next.next
            else:
                holder = holder.next
        return extra.next
