from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen_nodes = set()
        node = head
        seen_nodes.add(node)
        while node:
            node = node.next
            if node in seen_nodes:
                return node
            seen_nodes.add(node)
        return None
  