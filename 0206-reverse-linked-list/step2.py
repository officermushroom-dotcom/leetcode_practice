class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        node = head
        reversed_nodes = None
        while node is not None:
            temp_next_node = node.next
            node.next = reversed_nodes
            reversed_nodes = node
            node = temp_next_node
        return reversed_nodes
    