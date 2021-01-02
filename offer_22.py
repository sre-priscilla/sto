# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p, q = head, head
        for _ in range(k):
            q = q.next
        while not (q is None):
            p, q = p.next, q.next
        return p


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next= ListNode(4)
    head.next.next.next.next = ListNode(5)

    assert Solution().getKthFromEnd(head, 2).val == 4