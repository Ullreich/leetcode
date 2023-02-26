import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printself(self):
        print(self.val)
        if self.next != None:
            self.next.printself()

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        r = findmiddle(node)
        print(f"r is {r}")

        for i in range(r):
            node = node.next

        return node
def findmiddle(head: ListNode) -> int:
    r = 0

    node = head
    while node.next != None:
        node = node.next
        r = r+1

    #return int(r/2)
    return int(math.ceil(r/2))

l1 = ListNode(val= 2, next= ListNode(val= 4, next= ListNode(val= 3, next= None)))
l2 = ListNode(val= 2, next= ListNode(val= 4, next= None))


sol = Solution.middleNode(0, l2)
sol.printself()