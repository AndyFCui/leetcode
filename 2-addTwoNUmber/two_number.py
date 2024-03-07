from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy: ListNode = ListNode(-1)
        carryBit: int = 0 # its only 0 or 1
        cur: ListNode = dummy

        while l1 is not None or l2 is not None:
            # get list1 value
            if None == l1:
                x: int = 0
            else:
                x = l1.val

            # get list2 value
            if None == l2:
                y:int = 0
            else:
                y = l2.val

            # Operate
            sumValue: int = x + y + carryBit
            carryBit = sumValue // 10
            digit: int = sumValue % 10
            digit_node: ListNode = ListNode(digit)

            cur.next = digit_node
            cur = cur.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

            # if pointer move to none, we need to check carry bit
            if 1 == carryBit:
                carryBit_node: ListNode = ListNode(carryBit)
                cur.next = carryBit_node

        return dummy.next

# This time complex should be O(1), its depends on the size of data.

