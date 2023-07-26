# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next.next if head.next else None

        while fast:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next if fast.next else None

        return False
