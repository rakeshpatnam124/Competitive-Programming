# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        temp=head
        while temp:
            stack.append(temp)
            temp=temp.next
        i=0
        j=len(stack)-1
        flag=True
        while i<j:
            if (stack[i].val!=stack[j].val):
                flag=False
                break
            i+=1
            j-=1
        return flag
