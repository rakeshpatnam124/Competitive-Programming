# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = ListNode(0)
        temp=prev
        while head:
            if head.val!=val:
                prev.next=head
                prev=prev.next
            head=head.next
        prev.next=None
        return temp.next
