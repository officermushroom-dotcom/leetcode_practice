class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        new_head = ListNode(0, head)
        new_node = new_head
        node = head 
        while node is not None and node.next is not None:
            if node.val != node.next.val:
                new_node = new_node.next
            else:
                while node.next is not None and node.val == node.next.val:
                    node = node.next
                new_node.next = node.next
            node = node.next
        return new_head.next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        new_head = ListNode(0, head)
        node = new_head
        while node.next is not None and node.next.next is not None:
            if node.next.val != node.next.next.val:
                node = node.next
                continue
            duplicate_num = node.next.val
            while node.next is not None and node.next.val == duplicate_num:
                node.next = node.next.next
        return new_head.next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        distinct_nodes = []
        previous_node = None
        node = head
        while node is not None:
            differs_from_previous = previous_node is None or node.val != previous_node.val
            differs_from_next = node.next is None or node.next.val != node.val
            if differs_from_previous is True and differs_from_next is True:
                distinct_nodes.append(node)
            previous_node = node
            node = node.next

        new_head = ListNode()
        new_node = new_head
        for distinct_node in distinct_nodes:
            new_node.next = distinct_node
            new_node = new_node.next
        new_node.next = None
        return new_head.next
