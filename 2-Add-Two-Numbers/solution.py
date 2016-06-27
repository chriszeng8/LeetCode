# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        carry=0
        head=l1
        while l1.next and l2.next:
            l1.val,carry=(l1.val+l2.val+carry)%10,(l1.val+l2.val+carry)/10
            l1,l2=l1.next,l2.next
        l1.val,carry=(l1.val+l2.val+carry)%10,(l1.val+l2.val+carry)/10
        if l2.next:
            l1.next=l2.next
            l1=l1.next
        elif l1.next:
            l1=l1.next
        elif carry>0:
            l1.next=ListNode(1)
            l1.next.next=None
            return head
        while l1.next:
            l1.val,carry=(l1.val+carry)%10,(l1.val+carry)/10
            l1=l1.next
        l1.val,carry=(l1.val+carry)%10,(l1.val+carry)/10
        if carry>0:
            l1.next=ListNode(1)
            l1.next.next=None
        return head