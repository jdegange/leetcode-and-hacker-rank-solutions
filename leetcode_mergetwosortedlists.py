# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if (h1.val < h2.val):
            h1.next = self.mergeTwoLists(h1.next, h2)
            return h1
        else:
            h2.next = self.mergeTwoLists(h2.next, h1)
            return h2

