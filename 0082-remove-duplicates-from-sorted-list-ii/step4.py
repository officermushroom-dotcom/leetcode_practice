class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        while head is not None and head.next is not None and head.val == head.next.val:
            duplicate_val = head.val
            while head is not None and head.val == duplicate_val:
                head = head.next
        if head is None:
            return None

        previous_node = head
        node = head.next
        while node is not None:
            if node.next is not None and node.val == node.next.val:
                duplicate_val = node.val
                while node is not None and node.val == duplicate_val:
                    node = node.next
                previous_node.next = node  
            else:
                previous_node = node
                node = node.next
        return head
    