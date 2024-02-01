# Attempt 1: Naive solution by replacing the node value with some indicator value
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head

        while temp is not None:
            if temp.val == float('inf'):
                return True
            temp.val = float('inf')
            temp = temp.next
        return False


# Attempt 2: Simple solution without loosing the previous node information
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head

        while temp is not None:
            if temp.val > 10e5:
                return True
            temp.val += 10e6
            temp = temp.next
        return False
