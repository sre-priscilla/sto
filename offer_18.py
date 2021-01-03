# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        p, vals = self, []
        while p:
            vals.append(p.val)
            p = p.next
        return vals


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        zero = ListNode(0)
        zero.next = head

        prev, curr = zero, head
        while not (curr is None):
            if curr.val != val:
                prev, curr = curr, curr.next
            else:
                prev.next = curr.next
                break
        return zero.next


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    print(Solution().deleteNode(head, 5).to_list())