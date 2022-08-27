# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        revlist = list()

        while head.next != None:
            revlist.append(head.val)
            head = head.next
        revlist.append(head.val)

        return revlist == revlist[::-1]