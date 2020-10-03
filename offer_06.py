from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ret = []
        curr = head
        while curr:
            ret.append(curr.val)
            curr = curr.next
        ret.reverse()
        return ret