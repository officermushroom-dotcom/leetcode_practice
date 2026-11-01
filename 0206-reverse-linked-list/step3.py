class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        node = head
        previuos_node = None
        while node is not None:
            temp_next_node = node.next
            node.next = previuos_node
            previuos_node = node
            node = node.next
        return previuos_node
