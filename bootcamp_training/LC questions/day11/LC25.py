#reverse node in kth group
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while True:
            # Check k nodes available hain ya nahi
            kth = prev

            for i in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            group_next = kth.next

            # Reverse group
            curr = prev.next
            before = group_next

            while curr != group_next:
                temp = curr.next
                curr.next = before
                before = curr
                curr = temp

            # Connect previous part with reversed group
            temp = prev.next
            prev.next = kth
            prev = temp
        