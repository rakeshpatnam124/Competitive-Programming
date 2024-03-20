# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack=[]
        temp=head
        while temp:
            stack.append(temp.val)
            temp=temp.next
        dec=0
        i=0
        while stack:
            dec+=(2**i*stack.pop())
            i+=1
        return int(dec)
