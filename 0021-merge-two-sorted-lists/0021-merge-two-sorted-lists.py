# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        elif not list1:
            return list2
        elif not list2:
            return list1

        head = list1
        if list2.val < list1.val:
            head = list2
            while list1:
                if not list2.next:
                    list2.next = list1
                    return head
                elif list1.val <= list2.next.val:
                    tmp = list1
                    list1, tmp.next = list1.next, list2.next
                    list2.next = tmp
                else:
                    list2 = list2.next
            return head
        else:
            while list2:
                if not list1.next:
                    list1.next = list2
                    return head
                elif list2.val <= list1.next.val:
                    tmp = list2
                    list2, tmp.next = list2.next, list1.next
                    list1.next = tmp
                else:
                    list1 = list1.next
            return head
        