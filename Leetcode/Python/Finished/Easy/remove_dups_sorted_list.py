# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        holder = head
        extra = holder
        while extra != None and extra.next != None:
            if extra.val == extra.next.val:
                extra.next = extra.next.next
            else:
                extra = extra.next
        return holder
