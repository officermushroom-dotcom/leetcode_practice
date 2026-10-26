from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen_nodes = set()
        node = head
        if not node:
            return None
        while node:
            if node in seen_nodes:
                return node
            seen_nodes.add(node)
            node = node.next
        return None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                start = head
                while start is not slow:
                    start = start.next
                    slow = slow.next
                return start
        return None
        