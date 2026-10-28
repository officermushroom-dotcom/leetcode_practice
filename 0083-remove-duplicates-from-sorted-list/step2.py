
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        seen_node = set()
        node = head
        new_head = ListNode(None)
        new_node = new_head
        while node is not None:
            if node.val not in seen_node:
                new_node.next = ListNode(node.val)
                new_node = new_node.next
                seen_node.add(node.val)
            node = node.next
        return new_head.next
