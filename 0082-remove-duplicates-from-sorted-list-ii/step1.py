class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        new_head = ListNode(0, head)
        new_node = new_head
        node = head
        while node is not None:
            if node.next is not None and node.val == node.next.val:
                while node.next is not None and node.val == node.next.val:
                    node = node.next
                new_node.next = node.next
            else:
                new_node = new_node.next
            node = node.next
        return new_head.next  
    