class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 不正解のコード
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        node_1 = l1
        node_2 = l2
        result_head = ListNode()
        result_node = result_head
        carring = 0
        while node_1 and node_2:
            plused_num = node_1.val + node_2.val + carring
            if plused_num >= 10:
                result_node.val = plused_num - 10
                carring = 1
            else:
                result_node.val = plused_num
                carring = 0
            result_node = result_node.next
            node_1 = node_1.next
            node_2 = node_2.next
        if node_1 is not None:
            rest_node = node_1
        else:
            rest_node = node_2
        while rest_node is not None:
            plused_num = rest_node.val + carring
            if plused_num >= 10:
                result_node.val = plused_num - 10
                carring = 1
            else:
                result_node = plused_num
                carring = 0
            rest_node = rest_node.next
        return result_head.next
