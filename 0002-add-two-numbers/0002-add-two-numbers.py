# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        w1,w2=l1,l2
        l3 = ListNode()
        w3=l3
        carry = 0
        while w1 != None or w2 != None or carry==1:
            if w1==None and w2==None:
                result=0
            elif w1==None:
                result=w2.val
                w2=w2.next
            elif w2==None:
                result=w1.val
                w1=w1.next
            else:
                result = w1.val + w2.val
                w1,w2=w1.next,w2.next
            result+=carry
            carry=0
            if result > 9:
                carry=1
                result-=10
            w3.next=ListNode(result)
            w3=w3.next
        return l3.next