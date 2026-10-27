class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        new_head = ListNode(0, head)
        node = new_head
        while node.next is not None and node.next.next is not None:
            if node.next.val != node.next.next.val:
                node = node.next
                continue
            duplicates_num = node.next.val
            while node.next is not None and node.next.val == duplicates_num:
                node.next = node.next.next
        return new_head.next
