class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val) + ', ' + str(self.next)


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        base = ListNode(0)
        base.next = head

        current = base

        while True:
            block, nxt = self.get_next_k(current, k)
            if block is None:
                break

            for i in range(k - 1, -1, -1):
                if i == 0:
                    block[i].next = nxt
                else:
                    block[i].next = block[i - 1]

            current.next = block[-1]
            current = block[0]

        return base.next

    @staticmethod
    def get_next_k(current: ListNode, k: int) -> ([ListNode], ListNode):
        ret = []
        n = current
        for i in range(k):
            n = n.next
            if n is None:
                return None, None
            ret.append(n)

        return ret, ret[-1].next


sol = Solution()
lst = [1, 2, 3, 4, 5]

head = ListNode(lst[0])
current = head
for val in lst[1:]:
    n = ListNode(val)
    current.next = n
    current = n

print(sol.reverseKGroup(head, 2))
