class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1,l2)
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            print(l1)
            return l1
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            print(l2)
            return l2

list1 = [1,2,3,7]
list2 = [4,8,9]
answer = Solution()
answer.mergeTwoLists(l1=list1,l2=list2)