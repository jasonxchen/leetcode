# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            return_node = ListNode(head.val)
            curr_node = head.next
            while curr_node:
                return_node = ListNode(curr_node.val, return_node)
                curr_node = curr_node.next
            return return_node
        else:
            return head
