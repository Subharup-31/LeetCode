# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node is made to track the first element
        dummyNode = ListNode()
        curr  = dummyNode
        carry = 0

        while l1 or l2 or carry :
            #if there are no elements present
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            # if there is a carry , basically carry should be coutiung the carry value
            carry = val // 10
            val = val % 10
            # storigng it in a new linked list
            curr.next = ListNode(val)

            #updating the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return dummyNode.next


        