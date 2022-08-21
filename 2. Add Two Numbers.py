# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

     def printself(self):
         print(self.val)
         if self.next != None:
             self.next.printself()

# try recursion
def rec(l1: ListNode, l2: ListNode, carryover: int = 0) -> ListNode:
    value = l1.val + l2.val + carryover

    if l1.next == None and l2.next == None:
        if value > 9:
            return ListNode(val=value-10, next=ListNode(1, None))
        return ListNode(val=value, next=None)

    elif l1.next == None:
        if value > 9:
            return ListNode(val=value-10, next=rec(ListNode(0, None), l2.next, 1))
        return ListNode(val=value, next=l2.next)

    elif l2.next == None:
        if value > 9:
            return ListNode(val=value-10, next=rec(l1.next, ListNode(0, None), 1))
        return ListNode(val=value, next=l1.next)

    else:
        if value > 9:
            return ListNode(val=value-10, next=rec(l1.next, l2.next, 1))
        return ListNode(val=value, next=rec(l1.next, l2.next, 0))



l1 = ListNode(val= 2, next= ListNode(val= 4, next= ListNode(val= 3, next= None)))
l2 = ListNode(val= 5, next= ListNode(val= 6, next= ListNode(val= 4, next= None)))

res = rec(l1, l2)
res.printself()