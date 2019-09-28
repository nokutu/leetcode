class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        base = ListNode(0)
        base.next = head

        current = base

        while current.next and current.next.next:
            third = current.next.next.next
            second = current.next.next
            first = current.next

            first.next = third
            second.next = first
            current.next = second

            current = first
        return base.next


