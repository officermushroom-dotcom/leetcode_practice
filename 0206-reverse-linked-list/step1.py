class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        all_nodes = []
        node = head
        while node is not None:
            all_nodes.append(node)
            node = node.next
        new_head = all_nodes.pop()
        new_node = new_head
        while all_nodes:
            next_node = all_nodes.pop()
            new_node.next = next_node
            new_node = new_node.next
        new_node.next = None
        return new_head

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
    